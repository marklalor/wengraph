load("//graph/schema:schema.bzl", "schema_sql")

package(default_visibility = ["//graph:schema"])

schema_sql(name = "a", src = "a.sql")
schema_sql(name = "b", src = "b.sql", deps = ["//graph/schema/definition/test:a"])
schema_sql(name = "c", src = "c.sql", deps = ["//graph/schema/definition/test:a"])
schema_sql(name = "d", src = "d.sql", deps = ["//graph/schema/definition/test:b", "//graph/schema/definition/test:c"])

#schema_sql(name = "all", deps = [
#    "//graph/schema/definition/test:a",
#    "//graph/schema/definition/test:b",
#    "//graph/schema/definition/test:c",
#    "//graph/schema/definition/test:d",
#])