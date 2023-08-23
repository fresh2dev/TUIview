import argparse

parser = argparse.ArgumentParser(
    prog="jq",
    description="jq - commandline JSON processor [version 1.6]",
    usage="jq [options] <jq filter> [file...]\n"
    "jq [options] --args <jq filter> [strings...]\n"
    "jq [options] --jsonargs <jq filter> [JSON_TEXTS...]",
    add_help=False,
)

parser.add_argument(
    "filter",
    metavar="<jq filter>",
    help="jq filter to apply to JSON inputs",
)
parser.add_argument("files", nargs="*", help="JSON files to process")
parser.add_argument(
    "--args",
    metavar="<jq filter>",
    dest="args_filter",
    help="jq filter to apply to string arguments instead of files",
)
parser.add_argument(
    "--jsonargs",
    metavar="<jq filter>",
    dest="json_args_filter",
    help="jq filter to apply to JSON arguments instead of files",
)
parser.add_argument("-c", action="store_true", help="compact output")
parser.add_argument(
    "-n",
    action="store_true",
    help="use 'null' as the single input value",
)
parser.add_argument(
    "-e",
    action="store_true",
    help="set the exit status code based on the output",
)
parser.add_argument(
    "-s",
    action="store_true",
    help="read all inputs into an array; apply filter to it",
)
parser.add_argument(
    "-r",
    action="store_true",
    help="output raw strings, not JSON texts",
)
parser.add_argument("-R", action="store_true", help="read raw strings, not JSON texts")
parser.add_argument("-C", action="store_true", help="colorize JSON")
parser.add_argument("-M", action="store_true", help="monochrome (don't colorize JSON)")
parser.add_argument("-S", action="store_true", help="sort keys of objects on output")
parser.add_argument("--tab", action="store_true", help="use tabs for indentation")
parser.add_argument(
    "--arg",
    metavar=("a", "v"),
    nargs=2,
    action="append",
    dest="variables",
    help="set variable $a to value <v>",
)
parser.add_argument(
    "--argjson",
    metavar=("a", "v"),
    nargs=2,
    action="append",
    dest="json_variables",
    help="set variable $a to JSON value <v>",
)
parser.add_argument(
    "--slurpfile",
    metavar=("a", "f"),
    nargs=2,
    action="append",
    dest="slurp_files",
    help="set variable $a to an array of JSON texts read from <f>",
)
parser.add_argument(
    "--rawfile",
    metavar=("a", "f"),
    nargs=2,
    action="append",
    dest="raw_files",
    help="set variable $a to a string consisting of the contents of <f>",
)
