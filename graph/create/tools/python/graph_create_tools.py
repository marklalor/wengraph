import sqlite3
import argparse
from os.path import basename

def get_argparse():
    parser = argparse.ArgumentParser(description='Create SQL base')
    parser.add_argument("--schema-definitions", nargs='*', default=[])
    parser.add_argument("--inputs", nargs='*', default=[])
    parser.add_argument("--output")
    return parser

def get_tools():
    args = get_argparse().parse_args()
    inputs = {basename(filepath): filepath for filepath in args.inputs}
    cursor, dump = get_sql_writer()
    return inputs, cursor, dump

def get_sql_writer():
    args = get_argparse().parse_args()

    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    for sql_schema_filepath in args.schema_definitions:
        with open(sql_schema_filepath, mode='r') as sql_schema_file:
            sql_script = sql_schema_file.read().replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS")
            cursor.executescript(sql_script)

    def dump():
        filepath = args.output
        with open(filepath, mode='w') as dump_file:
            for line in conn.iterdump():
                if line.startswith("INSERT INTO"):
                    dump_file.write(line)
                    dump_file.write("\n")

    return cursor, dump
