import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="tree",
    description="CLI implementation of the tree command",
    add_help=False,
)

# Listing options
parser.add_argument("-a", action="store_true", help="All files are listed.")
parser.add_argument("-d", action="store_true", help="List directories only.")
parser.add_argument(
    "-l",
    action="store_true",
    help="Follow symbolic links like directories.",
)
parser.add_argument(
    "-f",
    action="store_true",
    help="Print the full path prefix for each file.",
)
parser.add_argument("-x", action="store_true", help="Stay on current filesystem only.")
parser.add_argument(
    "-L",
    dest="level",
    type=int,
    help="Descend only level directories deep.",
)
parser.add_argument(
    "-R",
    action="store_true",
    help="Rerun tree when max dir level reached.",
)
parser.add_argument(
    "-P",
    dest="pattern",
    help="List only those files that match the pattern given.",
)
parser.add_argument(
    "-I",
    dest="exclude_pattern",
    help="Do not list files that match the given pattern.",
)
parser.add_argument(
    "--gitignore",
    action="store_true",
    help="Filter by using .gitignore files.",
)
parser.add_argument(
    "--ignore-case",
    action="store_true",
    help="Ignore case when pattern matching.",
)
parser.add_argument(
    "--matchdirs",
    action="store_true",
    help="Include directory names in -P pattern matching.",
)
parser.add_argument(
    "--metafirst",
    action="store_true",
    help="Print meta-data at the beginning of each line.",
)
parser.add_argument(
    "--info",
    action="store_true",
    help="Print information about files found in .info files.",
)
parser.add_argument(
    "--noreport",
    action="store_true",
    help="Turn off file/directory count at end of tree listing.",
)
parser.add_argument(
    "--charset",
    dest="charset",
    help="Use charset X for terminal/HTML and indentation line output.",
)
parser.add_argument(
    "--filelimit",
    dest="filelimit",
    type=int,
    help="Do not descend dirs with more than # files in them.",
)
parser.add_argument("-o", dest="output", help="Output to file instead of stdout.")

# File options
parser.add_argument(
    "-q",
    action="store_true",
    help="Print non-printable characters as '?'.",
)
parser.add_argument(
    "-N",
    action="store_true",
    help="Print non-printable characters as is.",
)
parser.add_argument(
    "-Q",
    action="store_true",
    help="Quote filenames with double quotes.",
)
parser.add_argument(
    "-p",
    action="store_true",
    help="Print the protections for each file.",
)
parser.add_argument(
    "-u",
    action="store_true",
    help="Displays file owner or UID number.",
)
parser.add_argument(
    "-g",
    action="store_true",
    help="Displays file group owner or GID number.",
)
parser.add_argument(
    "-s",
    action="store_true",
    help="Print the size in bytes of each file.",
)
parser.add_argument(
    "-h",
    action="store_true",
    help="Print the size in a more human readable way.",
)
parser.add_argument(
    "--si",
    action="store_true",
    help="Like -h, but use in SI units (powers of 1000).",
)
parser.add_argument(
    "-D",
    action="store_true",
    help="Print the date of last modification or (-c) status change.",
)
parser.add_argument(
    "--timefmt",
    dest="timefmt",
    help="Print and format time according to the format <f>.",
)
parser.add_argument(
    "-F",
    action="store_true",
    help="Appends '/', '=', '*', '@', '|' or '>' as per ls -F.",
)
parser.add_argument(
    "--inodes",
    action="store_true",
    help="Print inode number of each file.",
)
parser.add_argument(
    "--device",
    action="store_true",
    help="Print device ID number to which each file belongs.",
)

# Sorting options
parser.add_argument(
    "-v",
    action="store_true",
    help="Sort files alphanumerically by version.",
)
parser.add_argument(
    "-t",
    action="store_true",
    help="Sort files by last modification time.",
)
parser.add_argument(
    "-c",
    action="store_true",
    help="Sort files by last status change time.",
)
parser.add_argument("-U", action="store_true", help="Leave files unsorted.")
parser.add_argument("-r", action="store_true", help="Reverse the order of the sort.")
parser.add_argument(
    "--dirsfirst",
    action="store_true",
    help="List directories before files (-U disables).",
)
parser.add_argument(
    "--filesfirst",
    action="store_true",
    help="List files before directories (-U disables).",
)
parser.add_argument(
    "--sort",
    dest="sort",
    help="Select sort: name,version,size,mtime,ctime.",
)

# Graphics options
parser.add_argument("-i", action="store_true", help="Don't print indentation lines.")
parser.add_argument(
    "-A",
    action="store_true",
    help="Print ANSI lines graphic indentation lines.",
)
parser.add_argument(
    "-S",
    action="store_true",
    help="Print with CP437 (console) graphics indentation lines.",
)
parser.add_argument(
    "-n",
    action="store_true",
    help="Turn colorization off always (-C overrides).",
)
parser.add_argument("-C", action="store_true", help="Turn colorization on always.")

# XML/HTML/JSON options
parser.add_argument(
    "-X",
    action="store_true",
    help="Prints out an XML representation of the tree.",
)
parser.add_argument(
    "-J",
    action="store_true",
    help="Prints out an JSON representation of the tree.",
)
parser.add_argument(
    "-H",
    dest="baseHREF",
    help="Prints out HTML format with baseHREF as top directory.",
)
parser.add_argument(
    "-T",
    dest="title",
    help="Replace the default HTML title and H1 header with string.",
)
parser.add_argument(
    "--nolinks",
    action="store_true",
    help="Turn off hyperlinks in HTML output.",
)

# Input options
parser.add_argument(
    "--fromfile",
    action="store_true",
    help="Reads paths from files (.=stdin)",
)

# Miscellaneous options
parser.add_argument("--version", action="store_true", help="Print version and exit.")
