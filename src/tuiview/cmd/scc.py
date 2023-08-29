import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="scc",
    description="Sloc, Cloc and Code. Count lines of code in a directory with complexity estimation.",
    add_help=False,
)

# Add flags
parser.add_argument(
    "--avg-wage",
    type=int,
    default=56286,
    help="average wage value used for basic COCOMO calculation",
)
parser.add_argument(
    "--binary",
    action="store_true",
    help="disable binary file detection",
)
parser.add_argument(
    "--by-file",
    action="store_true",
    help="display output for every file",
)
parser.add_argument(
    "--ci",
    action="store_true",
    help="enable CI output settings where stdout is ASCII",
)
parser.add_argument(
    "--cocomo-project-type",
    type=str,
    default="organic",
    help='change COCOMO model type [organic, semi-detached, embedded, "custom,1,1,1,1"]',
)
parser.add_argument("--count-as", type=str, help="count extension as language")
parser.add_argument(
    "--currency-symbol",
    type=str,
    default="$",
    help="set currency symbol",
)
parser.add_argument("--debug", action="store_true", help="enable debug output")
parser.add_argument(
    "--eaf",
    type=float,
    default=1,
    help="the effort adjustment factor derived from the cost drivers",
)
parser.add_argument(
    "--exclude-dir",
    nargs="+",
    default=[".git", ".hg", ".svn"],
    help="directories to exclude",
)
parser.add_argument("-x", "--exclude-ext", nargs="+", help="ignore file extensions")
parser.add_argument(
    "--file-gc-count",
    type=int,
    default=10000,
    help="number of files to parse before turning the GC on",
)
parser.add_argument(
    "-f",
    "--format",
    type=str,
    default="tabular",
    help="set output format",
)
parser.add_argument(
    "--format-multi",
    type=str,
    help="have multiple format output overriding --format",
)
parser.add_argument("--gen", action="store_true", help="identify generated files")
parser.add_argument(
    "--generated-markers",
    nargs="+",
    default=["do not edit", "<auto-generated />"],
    help="string markers in head of generated files",
)
parser.add_argument("-i", "--include-ext", nargs="+", help="limit to file extensions")
parser.add_argument(
    "--include-symlinks",
    action="store_true",
    help="if set will count symlink files",
)
parser.add_argument(
    "-l",
    "--languages",
    action="store_true",
    help="print supported languages and extensions",
)
parser.add_argument(
    "--large-byte-count",
    type=int,
    default=1000000,
    help="number of bytes a file can contain before being removed from output",
)
parser.add_argument(
    "--large-line-count",
    type=int,
    default=40000,
    help="number of lines a file can contain before being removed from output",
)
parser.add_argument("--min", action="store_true", help="identify minified files")
parser.add_argument(
    "-z",
    "--min-gen",
    action="store_true",
    help="identify minified or generated files",
)
parser.add_argument(
    "--min-gen-line-length",
    type=int,
    default=255,
    help="number of bytes per average line for file to be considered minified or generated",
)
parser.add_argument(
    "--no-cocomo",
    action="store_true",
    help="remove COCOMO calculation output",
)
parser.add_argument(
    "-c",
    "--no-complexity",
    action="store_true",
    help="skip calculation of code complexity",
)
parser.add_argument(
    "-d",
    "--no-duplicates",
    action="store_true",
    help="remove duplicate files from stats and output",
)
parser.add_argument(
    "--no-gen",
    action="store_true",
    help="ignore generated files in output (implies --gen)",
)
parser.add_argument(
    "--no-gitignore",
    action="store_true",
    help="disables .gitignore file logic",
)
parser.add_argument(
    "--no-ignore",
    action="store_true",
    help="disables .ignore file logic",
)
parser.add_argument(
    "--no-large",
    action="store_true",
    help="ignore files over certain byte and line size set by max-line-count and max-byte-count",
)
parser.add_argument(
    "--no-min",
    action="store_true",
    help="ignore minified files in output (implies --min)",
)
parser.add_argument(
    "--no-min-gen",
    action="store_true",
    help="ignore minified or generated files in output (implies --min-gen)",
)
parser.add_argument(
    "--no-size",
    action="store_true",
    help="remove size calculation output",
)
parser.add_argument(
    "-M",
    "--not-match",
    nargs="+",
    help="ignore files and directories matching regular expression",
)
parser.add_argument(
    "-o",
    "--output",
    type=str,
    default="stdout",
    help="output filename",
)
parser.add_argument(
    "--overhead",
    type=float,
    default=2.4,
    help="set the overhead multiplier for corporate overhead",
)
parser.add_argument(
    "--remap-all",
    type=str,
    help="inspect every file and remap by checking for a string and remapping the language",
)
parser.add_argument(
    "--remap-unknown",
    type=str,
    help="inspect files of unknown type and remap by checking for a string and remapping the language",
)
parser.add_argument("--size-unit", type=str, default="si", help="set size unit")
parser.add_argument(
    "--sloccount-format",
    action="store_true",
    help="print a more SLOCCount like COCOMO calculation",
)
parser.add_argument("-s", "--sort", type=str, default="files", help="column to sort by")
parser.add_argument(
    "--sql-project",
    type=str,
    help="use supplied name as the project identifier for the current run",
)
parser.add_argument("-t", "--trace", action="store_true", help="enable trace output")
parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
parser.add_argument("--version", action="store_true", help="version for scc")
parser.add_argument(
    "-w",
    "--wide",
    action="store_true",
    help="wider output with additional statistics",
)