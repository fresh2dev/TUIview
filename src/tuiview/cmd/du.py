import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="du",
    description="estimate file space usage",
    add_help=False,
)

# Add options
parser.add_argument("FILE", nargs="*", help="set of FILEs")
parser.add_argument(
    "-0",
    "--null",
    action="store_true",
    help="end each output line with NUL, not newline",
)
parser.add_argument(
    "-a",
    "--all",
    action="store_true",
    help="write counts for all files, not just directories",
)
parser.add_argument(
    "--apparent-size",
    action="store_true",
    help="print apparent sizes, rather than disk usage",
)
parser.add_argument(
    "-B",
    "--block-size",
    metavar="SIZE",
    help="scale sizes by SIZE before printing them",
)
parser.add_argument(
    "-b",
    "--bytes",
    action="store_true",
    help="equivalent to --apparent-size --block-size=1",
)
parser.add_argument("-c", "--total", action="store_true", help="produce a grand total")
parser.add_argument(
    "-D",
    "--dereference-args",
    action="store_true",
    help="dereference only symlinks that are listed on the command line",
)
parser.add_argument(
    "-d",
    "--max-depth",
    metavar="N",
    help="print the total for a directory only if it is N or fewer levels below the command line argument",
)
parser.add_argument(
    "--files0-from",
    metavar="F",
    help="summarize disk usage of the NUL-terminated file names specified in file F",
)
parser.add_argument("-H", action="store_true", help="equivalent to --dereference-args")
parser.add_argument(
    "-h",
    "--human-readable",
    action="store_true",
    help="print sizes in human readable format",
)
parser.add_argument(
    "--inodes",
    action="store_true",
    help="list inode usage information instead of block usage",
)
parser.add_argument("-k", action="store_true", help="like --block-size=1K")
parser.add_argument(
    "-L",
    "--dereference",
    action="store_true",
    help="dereference all symbolic links",
)
parser.add_argument(
    "-l",
    "--count-links",
    action="store_true",
    help="count sizes many times if hard linked",
)
parser.add_argument("-m", action="store_true", help="like --block-size=1M")
parser.add_argument(
    "-P",
    "--no-dereference",
    action="store_true",
    help="don't follow any symbolic links",
)
parser.add_argument(
    "-S",
    "--separate-dirs",
    action="store_true",
    help="for directories do not include size of subdirectories",
)
parser.add_argument(
    "--si",
    action="store_true",
    help="like -h, but use powers of 1000 not 1024",
)
parser.add_argument(
    "-s",
    "--summarize",
    action="store_true",
    help="display only a total for each argument",
)
parser.add_argument(
    "-t",
    "--threshold",
    metavar="SIZE",
    help="exclude entries smaller or greater than SIZE",
)
parser.add_argument(
    "--time",
    metavar="WORD",
    help="show time of the last modification of any file in the directory, or any of its subdirectories",
)
parser.add_argument("--time-style", metavar="STYLE", help="show times using STYLE")
parser.add_argument(
    "-X",
    "--exclude-from",
    metavar="FILE",
    help="exclude files that match any pattern in FILE",
)
parser.add_argument(
    "--exclude",
    metavar="PATTERN",
    help="exclude files that match PATTERN",
)
parser.add_argument(
    "-x",
    "--one-file-system",
    action="store_true",
    help="skip directories on different file systems",
)
parser.add_argument("--version", action="version", version="%(prog)s 8.32")
