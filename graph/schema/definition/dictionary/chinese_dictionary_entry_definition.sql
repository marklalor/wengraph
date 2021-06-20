CREATE TABLE "ChineseDictionaryEntryDefinition"
(
    "hash"              uuid      NOT NULL PRIMARY KEY,
    "definition"        text      NOT NULL,
    "entry_hash"        text      NOT NULL,
    "source"            text      NOT NULL,
    FOREIGN KEY (source) REFERENCES "Source" (name),
    FOREIGN KEY (entry_hash) REFERENCES "ChineseDictionaryEntry" (hash)
);
