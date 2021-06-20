load("//graph/schema:schema.bzl", "schema_sql")

package(default_visibility = ["//graph:schema"])

schema_sql(
    name = "glotto_language",
    src = "glotto_language.sql",
    deps = ["//graph/schema/definition:source"]
)

#schema_sql(name = "all", deps = ":glotto_language")