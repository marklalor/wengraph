from itertools import chain

from graph.create.tools.python.graph_create_tools import get_tools
import uuid

inputs, cursor, dump = get_tools()

with open(inputs["cedict_ts.u8"], mode='r') as cedict_txt_file:
    # cedict = list(filter(lambda line: not line.startswith("#"), [next(cedict_txt_file) for x in range(203)]))
    cedict = list(filter(lambda line: not line.startswith("#"), cedict_txt_file.readlines()))

print(cedict[-1])

def parse_cedict_line(line):
    line_remaining = line

    first_space_index = line_remaining.index(" ")
    traditional = line_remaining[0:first_space_index]
    line_remaining = line_remaining[first_space_index + 1:]

    second_space_index = line_remaining.index(" ")
    simplified = line_remaining[0:second_space_index]
    line_remaining = line_remaining[second_space_index + 2:]

    right_bracket_index = line_remaining.index("]")
    pinyin = line_remaining[0:right_bracket_index].replace("u:", "v")
    line_remaining = line_remaining[right_bracket_index + 3:]

    remove_empty = lambda definition: definition != ""
    entry_definitions = list(filter(remove_empty, line_remaining[0:len(line_remaining) - 1].split("/")))
    hash = uuid.uuid5(uuid.UUID("5c5bcbe5-b69e-4093-9ecf-3bce778d8e73"), f"${traditional}:${simplified}:${pinyin}").bytes
    return (hash, traditional, simplified, pinyin), entry_definitions

entries_with_definitions = map(parse_cedict_line, cedict)

entries, entry_definitions = zip(*entries_with_definitions)

def parse_definitions(definitions, entry):
    def parse_definition(definition):
        entry_hash, _, _, _ = entry
        hash = uuid.uuid5(uuid.UUID("5c5bcbe5-b69e-4093-9ecf-3bce778d8e74"), f"${entry_hash}:${definition}").bytes
        return hash, definition, entry_hash, "cc-cedict"
    return list(map(parse_definition, definitions))


definitions = list(chain(*map(parse_definitions, entry_definitions, entries)))

cursor.execute("""
INSERT INTO "Source" ("name", "full_name", "description", "homepage", "license") VALUES ("cc-cedict", "", "online, downloadable public-domain Chinese-English dictionary", "homepage", "CC BY-SA 3.0")
""")

cursor.executemany("""
INSERT INTO ChineseDictionaryEntry ("hash", "simplified", "traditional", "pinyin") VALUES (?, ?, ?, ?)
""", entries)

cursor.executemany("""
INSERT INTO ChineseDictionaryEntryDefinition ("hash", "definition", "entry_hash", "source") VALUES (?, ?, ?, ?)
""", definitions)

# cursor.executemany("""
# INSERT INTO ChineseDictionaryEntryDefinitionReference ("definition_hash", "entry_hash") VALUES (?, ?)
# """, definitions)

dump()