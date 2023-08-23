import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="df",
    description="report file system disk space usage",
    add_help=False,
)

# Add arguments
parser.add_argument("file", nargs="*", help="file name argument")
parser.add_argument(
    "-a",
    "--all",
    action="store_true",
    help="include pseudo, duplicate, inaccessible file systems",
)
parser.add_argument(
    "-B",
    "--block-size",
    metavar="SIZE",
    help="scale sizes by SIZE before printing them",
)
parser.add_argument(
    "-h",
    "--human-readable",
    action="store_true",
    help="print sizes in powers of 1024",
)
parser.add_argument(
    "-H",
    "--si",
    action="store_true",
    help="print sizes in powers of 1000",
)
parser.add_argument(
    "-i",
    "--inodes",
    action="store_true",
    help="list inode information instead of block usage",
)
parser.add_argument("-k", action="store_true", help="like --block-size=1K")
parser.add_argument(
    "-l",
    "--local",
    action="store_true",
    help="limit listing to local file systems",
)
parser.add_argument(
    "--no-sync",
    action="store_true",
    help="do not invoke sync before getting usage info",
)
parser.add_argument(
    "--output",
    metavar="FIELD_LIST",
    help="use the output format defined by FIELD_LIST",
)
parser.add_argument(
    "-P",
    "--portability",
    action="store_true",
    help="use the POSIX output format",
)
parser.add_argument(
    "--sync",
    action="store_true",
    help="invoke sync before getting usage info",
)
parser.add_argument(
    "--total",
    action="store_true",
    help="elide all entries insignificant to available space, and produce a grand total",
)
parser.add_argument(
    "-t",
    "--type",
    metavar="TYPE",
    help="limit listing to file systems of type TYPE",
)
parser.add_argument(
    "-T",
    "--print-type",
    action="store_true",
    help="print file system type",
)
parser.add_argument(
    "-x",
    "--exclude-type",
    metavar="TYPE",
    help="limit listing to file systems not of type TYPE",
)
parser.add_argument("-v", action="store_true", help="(ignored)")
parser.add_argument("--version", action="version", version="%(prog)s 8.32")
