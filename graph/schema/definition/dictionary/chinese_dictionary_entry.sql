CREATE TABLE "ChineseDictionaryEntry"
(
    hash           uuid NOT NULL PRIMARY KEY,
    traditional    text NOT NULL,
    simplified     text NOT NULL,
    pinyin         text NOT NULL
--     UNIQUE (traditional, pinyin),
--     UNIQUE (simplified, pinyin)
);