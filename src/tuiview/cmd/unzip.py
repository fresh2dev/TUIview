import argparse

parser = argparse.ArgumentParser(
    prog="unzip",
    description="UnZip 6.00 of 20 April 2009, by Debian. Original by Info-ZIP.",
    add_help=False,
)

# Arguments
parser.add_argument(
    "files",
    metavar="list",
    nargs="+",
    help="list of files to extract",
)
parser.add_argument(
    "-x",
    metavar="xlist",
    help="exclude files that follow (in xlist)",
)
parser.add_argument("-d", metavar="exdir", help="extract files into exdir")

# Options
parser.add_argument("-Z", action="store_true", help="ZipInfo mode")
parser.add_argument(
    "-p",
    action="store_true",
    help="extract files to pipe, no messages",
)
parser.add_argument("-l", action="store_true", help="list files (short format)")
parser.add_argument(
    "-f",
    action="store_true",
    help="freshen existing files, create none",
)
parser.add_argument("-t", action="store_true", help="test compressed archive data")
parser.add_argument("-u", action="store_true", help="update files, create if necessary")
parser.add_argument("-z", action="store_true", help="display archive comment only")
parser.add_argument("-v", action="store_true", help="list verbosely/show version info")
parser.add_argument("-T", action="store_true", help="timestamp archive to latest")
parser.add_argument("-n", action="store_true", help="never overwrite existing files")
parser.add_argument("-q", action="store_true", help="quiet mode (-qq => quieter)")
parser.add_argument("-o", action="store_true", help="overwrite files WITHOUT prompting")
parser.add_argument("-a", action="count", help="auto-convert any text files")
parser.add_argument(
    "-j",
    action="store_true",
    help="junk paths (do not make directories)",
)
parser.add_argument(
    "-U",
    action="count",
    help="use escapes for all non-ASCII Unicode",
)
parser.add_argument(
    "-C",
    action="store_true",
    help="match filenames case-insensitively",
)
parser.add_argument("-L", action="store_true", help="make (some) names lowercase")
parser.add_argument("-X", action="store_true", help="restore UID/GID info")
parser.add_argument("-V", action="store_true", help="retain VMS version numbers")
parser.add_argument(
    "-K",
    action="store_true",
    help="keep setuid/setgid/tacky permissions",
)
parser.add_argument("-M", action="store_true", help='pipe through "more" pager')
parser.add_argument(
    "-O",
    metavar="CHARSET",
    help="specify a character encoding for DOS, Windows and OS/2 archives",
)
parser.add_argument(
    "-I",
    metavar="CHARSET",
    help="specify a character encoding for UNIX and other archives",
)
