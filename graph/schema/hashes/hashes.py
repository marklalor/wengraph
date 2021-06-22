import uuid

NAMESPACE_WENGRAPH = uuid.UUID("5c5bcbe5-b69e-4093-9ecf-3bce778d8e73")


def wengraph_uuid(*args):
    return uuid.uuid5(NAMESPACE_WENGRAPH, ":".join(args)).hex


def chinese_dictionary_entry(traditional, simplified, pinyin):
    return wengraph_uuid("ChineseDictionaryEntry", traditional, simplified, pinyin)


def chinese_dictionary_entry_definition(entry_hash, definition):
    return wengraph_uuid("ChineseDictionaryEntry", entry_hash, definition)
