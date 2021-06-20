load("//graph/create/tools:tools.bzl", "generate_sql")

genrule(
  name = "cedict_unzipped",
  srcs = ["@cedict_zip//file"],
  tools = ["@bazel_tools//tools/zip:zipper"],
  output_to_bindir = True,
  outs = ["cedict_ts.u8"],
  cmd = "$(location @bazel_tools//tools/zip:zipper) x $(SRCS) -d $$(dirname $@)",
)

py_binary(
    name = "cedict_binary",
    srcs = ["cedict_create.py"],
    main = "cedict_create.py",
    deps = ["//graph/create/tools/python:wengraph_create_tools"],
)

generate_sql(
    name = "cedict",
    binary = ":cedict_binary",
    tools = [":cedict_unzipped"],
    inputs = [":cedict_ts.u8"],
    schema_definitions =  [
        "//graph/schema/definition/dictionary:chinese_dictionary_entry",
        "//graph/schema/definition/dictionary:chinese_dictionary_entry_definition"
    ],
)
