load("//graph/schema:schema.bzl", "schema_sql")

package(default_visibility = ["//graph:schema"])

schema_sql(
    name = "chinese_dictionary_entry",
    src = "chinese_dictionary_entry.sql",
    deps = ["//graph/schema/definition:source"]
)

schema_sql(
    name = "chinese_dictionary_entry_definition",
    src = "chinese_dictionary_entry_definition.sql",
    deps = [":chinese_dictionary_entry", "//graph/schema/definition:source"]
)

schema_sql(
    name = "chinese_dictionary_entry_definition_reference",
    src = "chinese_dictionary_entry_definition_reference.sql",
    deps = [":chinese_dictionary_entry", ":chinese_dictionary_entry_definition"]
)