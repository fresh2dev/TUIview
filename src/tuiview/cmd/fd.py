import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="fd",
    description="A file searching tool",
    add_help=False,
)

# Create the command for the pattern and path arguments
parser.add_argument("pattern", nargs="?", help="The search pattern")
parser.add_argument("path", nargs="*", help="The paths to search in")

# Create the flags
parser.add_argument(
    "-H",
    "--hidden",
    action="store_true",
    help="Include hidden directories and files in the search results (default: hidden files and directories are skipped)",
)
parser.add_argument(
    "-I",
    "--no-ignore",
    action="store_true",
    help="Show search results from files and directories that would otherwise be ignored by '.gitignore', '.ignore', '.fdignore', or the global ignore file",
)
parser.add_argument(
    "--no-ignore-vcs",
    action="store_true",
    help="Show search results from files and directories that would otherwise be ignored by '.gitignore' files",
)
parser.add_argument(
    "--no-ignore-parent",
    action="store_true",
    help="Show search results from files and directories that would otherwise be ignored by '.gitignore', '.ignore', or '.fdignore' files in parent directories",
)
parser.add_argument(
    "-u",
    "--unrestricted",
    action="count",
    help="Alias for '-I'. Can be repeated. '-uu' is an alias for '--no-ignore --hidden'",
)
parser.add_argument(
    "-s",
    "--case-sensitive",
    action="store_true",
    help="Perform a case-sensitive search",
)
parser.add_argument(
    "-i",
    "--ignore-case",
    action="store_true",
    help="Perform a case-insensitive search",
)
parser.add_argument(
    "-g",
    "--glob",
    action="store_true",
    help="Perform a glob-based search instead of a regular expression search",
)
parser.add_argument(
    "--regex",
    action="store_true",
    help="Perform a regular-expression based search (default)",
)
parser.add_argument(
    "-F",
    "--fixed-strings",
    action="store_true",
    help="Treat the pattern as a literal string instead of a regular expression",
)
parser.add_argument(
    "-a",
    "--absolute-path",
    action="store_true",
    help="Shows the full path starting from the root as opposed to relative paths",
)
parser.add_argument(
    "-l",
    "--list-details",
    action="store_true",
    help="Use a detailed listing format like 'ls -l'",
)
parser.add_argument(
    "-L",
    "--follow",
    action="store_true",
    help="Traverse symbolic links",
)
parser.add_argument(
    "-p",
    "--full-path",
    action="store_true",
    help="Match the pattern against the full (absolute) path",
)
parser.add_argument(
    "-0",
    "--print0",
    action="store_true",
    help="Separate search results by the null character (instead of newlines)",
)
parser.add_argument(
    "--prune",
    action="store_true",
    help="Do not traverse into directories that match the search criteria",
)
parser.add_argument(
    "-1",
    action="store_true",
    help="Limit the search to a single result and quit immediately",
)
parser.add_argument(
    "-q",
    "--quiet",
    action="store_true",
    help="Return with an exit code of 0 if there is at least one match",
)
parser.add_argument(
    "--show-errors",
    action="store_true",
    help="Enable the display of filesystem errors",
)
parser.add_argument(
    "--strip-cwd-prefix",
    action="store_true",
    help="Disable prefixing relative paths with './'",
)
parser.add_argument(
    "--one-file-system",
    action="store_true",
    help="Ensure that fd does not descend into a different file system than the one it started in",
)
parser.add_argument(
    "-V",
    "--version",
    action="store_true",
    help="Prints version information",
)

# Create the options
parser.add_argument(
    "-d",
    "--max-depth",
    type=int,
    help="Limit the directory traversal to a given depth",
)
parser.add_argument(
    "--min-depth",
    type=int,
    help="Only show search results starting at the given depth",
)
parser.add_argument(
    "--exact-depth",
    type=int,
    help="Only show search results at the exact given depth",
)
parser.add_argument("-t", "--type", nargs="+", help="Filter the search by type")
parser.add_argument(
    "-e",
    "--extension",
    nargs="+",
    help="Filter search results by their file extension",
)
parser.add_argument(
    "-x",
    "--exec",
    nargs=argparse.REMAINDER,
    help="Execute a command for each search result in parallel",
)
parser.add_argument(
    "-X",
    "--exec-batch",
    nargs=argparse.REMAINDER,
    help="Execute the given command once, with all search results as arguments",
)
parser.add_argument(
    "--batch-size",
    type=int,
    help="Maximum number of arguments to pass to the command given with -X",
)
parser.add_argument(
    "-E",
    "--exclude",
    action="append",
    help="Exclude files/directories that match the given glob pattern",
)
parser.add_argument(
    "--ignore-file",
    action="append",
    help="Add a custom ignore-file in '.gitignore' format",
)
parser.add_argument(
    "-c",
    "--color",
    choices=["auto", "never", "always"],
    help="Declare when to use color for the pattern match output",
)
parser.add_argument(
    "-j",
    "--threads",
    type=int,
    help="Set number of threads to use for searching & executing",
)
parser.add_argument(
    "-S",
    "--size",
    help="Limit results based on the size of files",
)
parser.add_argument(
    "--changed-within",
    help="Filter results based on the file modification time",
)
parser.add_argument(
    "--changed-before",
    help="Filter results based on the file modification time",
)
