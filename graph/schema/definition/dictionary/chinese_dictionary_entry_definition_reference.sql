CREATE TABLE "ChineseDictionaryEntryDefinitionReference"
(
    "definition_hash"   uuid      NOT NULL PRIMARY KEY,
    "entry_hash"        uuid      NOT NULL,
    FOREIGN KEY (definition_hash) REFERENCES "ChineseDictionaryEntryDefinition" (hash),
    FOREIGN KEY (entry_hash) REFERENCES "ChineseDictionaryEntry" (hash)
);
