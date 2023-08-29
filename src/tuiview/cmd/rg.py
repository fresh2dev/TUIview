import argparse

parser = argparse.ArgumentParser(
    prog="rg",
    description="ripgrep (rg) recursively searches the current directory for a regex pattern",
    epilog="For more information, visit https://github.com/BurntSushi/ripgrep",
    add_help=False,
)

parser.add_argument(
    "pattern",
    metavar="PATTERN",
    help="A regular expression used for searching. To match a pattern beginning with a dash, use the -e/--regexp flag.",
)
parser.add_argument(
    "path",
    metavar="PATH",
    nargs="*",
    help="A file or directory to search. Directories are searched recursively. File paths specified on the command line override glob and ignore rules.",
)

group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-e",
    "--regexp",
    metavar="PATTERN",
    help="A regular expression pattern used for searching",
)
group.add_argument(
    "-f",
    "--file",
    metavar="PATTERNFILE",
    nargs="+",
    help="A file containing multiple regular expression patterns",
)

parser.add_argument(
    "--files",
    action="store_true",
    help="List all matching files without searching their contents",
)
parser.add_argument(
    "--type-list",
    action="store_true",
    help="List all supported file types for searching",
)

parser.add_argument(
    "-A",
    "--after-context",
    metavar="NUM",
    type=int,
    help="Show NUM lines after each match",
)
parser.add_argument(
    "--auto-hybrid-regex",
    action="store_true",
    help="(DEPRECATED) Automatically choose between supported regex engines",
)
parser.add_argument(
    "-B",
    "--before-context",
    metavar="NUM",
    type=int,
    help="Show NUM lines before each match",
)
parser.add_argument("--binary", action="store_true", help="Search binary files")
parser.add_argument(
    "--block-buffered",
    action="store_true",
    help="Use block buffering for output",
)
parser.add_argument(
    "-b",
    "--byte-offset",
    action="store_true",
    help="Print the byte offset within the input file before each line of output",
)
parser.add_argument(
    "-s",
    "--case-sensitive",
    action="store_true",
    help="Search case sensitively",
)
parser.add_argument(
    "--color",
    metavar="WHEN",
    choices=["never", "auto", "always", "ansi"],
    default="auto",
    help="Control when to use colors",
)
parser.add_argument(
    "--colors",
    nargs="+",
    metavar="COLOR_SPEC",
    help="Specify color settings for use in the output",
)
parser.add_argument("--column", action="store_true", help="Show column numbers")
parser.add_argument(
    "-C",
    "--context",
    metavar="NUM",
    type=int,
    help="Show NUM lines before and after each match",
)
parser.add_argument(
    "--context-separator",
    metavar="SEPARATOR",
    default="--",
    help="The string used to separate non-contiguous context lines in the output",
)
parser.add_argument(
    "-c",
    "--count",
    action="store_true",
    help="Show the number of lines that match the given patterns for each file searched",
)
