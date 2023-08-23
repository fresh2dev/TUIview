import argparse

# Create the argparse parser
parser = argparse.ArgumentParser(
    prog="diff",
    description="Compare FILES line by line.",
    add_help=False,
)

# Create the mutually exclusive group for the output format options
output_group = parser.add_mutually_exclusive_group()

# Add the options
parser.add_argument(
    "--normal",
    action="store_true",
    help="output a normal diff (the default)",
)
parser.add_argument(
    "-q",
    "--brief",
    action="store_true",
    help="report only when files differ",
)
parser.add_argument(
    "-s",
    "--report-identical-files",
    action="store_true",
    help="report when two files are the same",
)
parser.add_argument(
    "-c",
    "-C",
    "--context",
    nargs="?",
    const=3,
    type=int,
    help="output NUM (default 3) lines of copied context",
)
parser.add_argument(
    "-u",
    "-U",
    "--unified",
    nargs="?",
    const=3,
    type=int,
    help="output NUM (default 3) lines of unified context",
)
parser.add_argument("-e", "--ed", action="store_true", help="output an ed script")
parser.add_argument(
    "-n",
    "--rcs",
    action="store_true",
    help="output an RCS format diff",
)
parser.add_argument(
    "-y",
    "--side-by-side",
    action="store_true",
    help="output in two columns",
)
parser.add_argument(
    "-W",
    "--width",
    type=int,
    default=130,
    help="output at most NUM (default 130) print columns",
)
parser.add_argument(
    "--left-column",
    action="store_true",
    help="output only the left column of common lines",
)
parser.add_argument(
    "--suppress-common-lines",
    action="store_true",
    help="do not output common lines",
)
parser.add_argument(
    "-p",
    "--show-c-function",
    action="store_true",
    help="show which C function each change is in",
)
parser.add_argument(
    "-F",
    "--show-function-line",
    metavar="RE",
    help="show the most recent line matching RE",
)
parser.add_argument(
    "--label",
    metavar="LABEL",
    action="append",
    help="use LABEL instead of file name and timestamp (can be repeated)",
)
parser.add_argument(
    "-t",
    "--expand-tabs",
    action="store_true",
    help="expand tabs to spaces in output",
)
parser.add_argument(
    "-T",
    "--initial-tab",
    action="store_true",
    help="make tabs line up by prepending a tab",
)
parser.add_argument(
    "--tabsize",
    type=int,
    default=8,
    help="tab stops every NUM (default 8) print columns",
)
parser.add_argument(
    "--suppress-blank-empty",
    action="store_true",
    help="suppress space or tab before empty output lines",
)
parser.add_argument(
    "-l",
    "--paginate",
    action="store_true",
    help="pass output through 'pr' to paginate it",
)
parser.add_argument(
    "-r",
    "--recursive",
    action="store_true",
    help="recursively compare any subdirectories found",
)
parser.add_argument(
    "--no-dereference",
    action="store_true",
    help="don't follow symbolic links",
)
parser.add_argument(
    "-N",
    "--new-file",
    action="store_true",
    help="treat absent files as empty",
)
parser.add_argument(
    "--unidirectional-new-file",
    action="store_true",
    help="treat absent first files as empty",
)
parser.add_argument(
    "--ignore-file-name-case",
    action="store_true",
    help="ignore case when comparing file names",
)
parser.add_argument(
    "--no-ignore-file-name-case",
    action="store_true",
    help="consider case when comparing file names",
)
parser.add_argument(
    "-x",
    "--exclude",
    metavar="PAT",
    help="exclude files that match PAT",
)
parser.add_argument(
    "-X",
    "--exclude-from",
    metavar="FILE",
    help="exclude files that match any pattern in FILE",
)
parser.add_argument(
    "-S",
    "--starting-file",
    metavar="FILE",
    help="start with FILE when comparing directories",
)
parser.add_argument(
    "--from-file",
    metavar="FILE1",
    help="compare FILE1 to all operands; FILE1 can be a directory",
)
parser.add_argument(
    "--to-file",
    metavar="FILE2",
    help="compare all operands to FILE2; FILE2 can be a directory",
)
parser.add_argument(
    "-i",
    "--ignore-case",
    action="store_true",
    help="ignore case differences in file contents",
)
parser.add_argument(
    "-E",
    "--ignore-tab-expansion",
    action="store_true",
    help="ignore changes due to tab expansion",
)
parser.add_argument(
    "-Z",
    "--ignore-trailing-space",
    action="store_true",
    help="ignore white space at line end",
)
parser.add_argument(
    "-b",
    "--ignore-space-change",
    action="store_true",
    help="ignore changes in the amount of white space",
)
parser.add_argument(
    "-w",
    "--ignore-all-space",
    action="store_true",
    help="ignore all white space",
)
parser.add_argument(
    "-B",
    "--ignore-blank-lines",
    action="store_true",
    help="ignore changes where lines are all blank",
)
parser.add_argument(
    "-I",
    "--ignore-matching-lines",
    metavar="RE",
    help="ignore changes where all lines match RE",
)
parser.add_argument("-a", "--text", action="store_true", help="treat all files as text")
parser.add_argument(
    "--strip-trailing-cr",
    action="store_true",
    help="strip trailing carriage return on input",
)
parser.add_argument(
    "-D",
    "--ifdef",
    metavar="NAME",
    help="output merged file with '#ifdef NAME' diffs",
)
parser.add_argument(
    "--GTYPE-group-format",
    metavar="GFMT",
    help="format GTYPE input groups with GFMT",
)
parser.add_argument(
    "--line-format",
    metavar="LFMT",
    help="format all input lines with LFMT",
)
parser.add_argument(
    "--LTYPE-line-format",
    metavar="LFMT",
    help="format LTYPE input lines with LFMT",
)
parser.add_argument(
    "-d",
    "--minimal",
    action="store_true",
    help="try hard to find a smaller set of changes",
)
parser.add_argument(
    "--horizon-lines",
    metavar="NUM",
    type=int,
    help="keep NUM lines of the common prefix and suffix",
)
parser.add_argument(
    "--speed-large-files",
    action="store_true",
    help="assume large files and many scattered small changes",
)
parser.add_argument(
    "--color",
    nargs="?",
    const="auto",
    choices=["never", "always", "auto"],
    help="color output",
)
parser.add_argument(
    "--palette",
    metavar="PALETTE",
    help="the colors to use when --color is active; PALETTE is a colon-separated list of terminfo capabilities",
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s 1.0",
    help="output version information and exit",
)

# Add the positional argument
parser.add_argument(
    "files",
    nargs="+",
    help="FILES are 'FILE1 FILE2' or 'DIR1 DIR2' or 'DIR FILE' or 'FILE DIR'",
)
