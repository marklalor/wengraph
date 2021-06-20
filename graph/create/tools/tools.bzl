def generate_sql(name, tools, inputs, schema_definitions, binary):
    native.genrule(
      name = name,
      tools = [binary] + tools,
      srcs = inputs + schema_definitions,
      outs = [name + ".sql"],
      cmd = "$(location " + binary + ") "
      + "--schema-definitions " + " ".join(["$(locations " + target + ")" for target in schema_definitions])
      + " --inputs " + " ".join(["$(locations " + target + ")" for target in inputs])
      + " --output $@"
    )
