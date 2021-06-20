TransitiveSqlFiles = provider("transitive_sources")
SqlFileList = provider("schema_sql_list")

def _schema_sql_files_impl(ctx):
    trans_srcs = depset(
        ctx.files.src,
        transitive = [dep[TransitiveSqlFiles].transitive_sources for dep in ctx.attr.deps],
        order = "topological"
    )
    output_file = ctx.actions.declare_file("schema_" + ctx.label.name + ".sql")
    output_list_file = ctx.actions.declare_file("schema_sql_list_" + ctx.label.name)


    trans_srcs_paths = [file.path for file in reversed(trans_srcs.to_list())]
    ctx.actions.run_shell(
        inputs = trans_srcs,
        outputs = [output_file],
        mnemonic = "concatSQL",
        progress_message = "Concatenating SQL",
        command = " ".join(["cat"] + [file.path for file in reversed(trans_srcs.to_list())] + [">", output_file.path])
    )

    ctx.actions.write(
        output = output_list_file,
        content = "\n".join(trans_srcs_paths) + "\n"
    )

    return [
        TransitiveSqlFiles(transitive_sources = trans_srcs),
        SqlFileList(schema_sql_list = depset([output_list_file])),
        DefaultInfo(files = depset([output_file]))
    ]


schema_sql = rule(
    implementation = _schema_sql_files_impl,
    attrs = {
        "src": attr.label(allow_single_file = [".sql"]),
        "deps": attr.label_list(allow_files = False),
    },
)

def _create_full_schema_impl(ctx):
    output_file = ctx.actions.declare_file("full_schema_" + ctx.label.name + ".sql")
    schema_list_depsets = [dep[SqlFileList].schema_sql_list for dep in ctx.attr.deps]
    schema_list_files_lists = [schema_list_depset.to_list() for schema_list_depset in schema_list_depsets]
    schema_list_files = [schema_list_files_list[0] for schema_list_files_list in schema_list_files_lists]

    ctx.actions.run_shell(
        inputs = schema_list_files,
        outputs = [output_file],
        mnemonic = "dedupeSQLS",
        progress_message = "Deduping SQL Schema",
        command = " ".join(["cat"] + [file.path for file in schema_list_files] + ["|", "awk '!x[$0]++'", "|", "xargs", "cat", ">", output_file.path])
    )

    return [
        DefaultInfo(files = depset([output_file]))
    ]


create_full_schema = rule(
    implementation = _create_full_schema_impl,
    attrs = {
        "deps": attr.label_list(allow_files = False, providers = [SqlFileList, TransitiveSqlFiles]),
    },
)