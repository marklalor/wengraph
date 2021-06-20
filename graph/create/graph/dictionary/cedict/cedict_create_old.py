import sys
import sqlite3

cedict_txt_path = sys.argv[1]
cedict_sql_path = sys.argv[2]

def parse(line):
    lineRemaining = line;

    firstSpaceIndex = lineRemaining.index(" ");
    traditional = lineRemaining[0:firstSpaceIndex];
    lineRemaining = lineRemaining[firstSpaceIndex + 1:];

    secondSpaceIndex = lineRemaining.index(" ");
    simplified = lineRemaining[0:secondSpaceIndex];
    lineRemaining = lineRemaining[secondSpaceIndex + 2:];

    rightBracketIndex = lineRemaining.index("]");
    pronunciation = lineRemaining[0:rightBracketIndex].replace("u:", "v");
    lineRemaining = lineRemaining[rightBracketIndex + 3:];

    definitions = list(filter(lambda definition: definition != "", lineRemaining[0:len(lineRemaining) - 1].split("/")))
    return ((traditional, simplified, pronunciation), definitions)

with open(cedict_txt_path, mode='r') as cedict_txt_file:
    head = filter(lambda line: not line.startswith("#"), [next(cedict_txt_file) for x in range(132)])

entriesAndDefinitions = map(parse, head)
entries = list(map(lambda entryAndDefinition: entryAndDefinition[0], entriesAndDefinitions))

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE "ChineseDictionaryEntry"
(

    simplified     text NOT NULL PRIMARY KEY,
    traditional    text NOT NULL,
    pinyin         text NOT NULL,
    UNIQUE (simplified,traditional,pinyin)
);
""")

cursor.executemany("""
INSERT INTO ChineseDictionaryEntry ("simplified", "traditional", "pinyin") VALUES (?, ?, ?)
""", entries)

with open(cedict_sql_path, mode='w') as cedict_sql_file:
    for line in conn.iterdump():
        cedict_sql_file.write('%s\n' % line)

