import yapx
from argparse_tui import invoke_tui


def rsync() -> yapx.ArgumentParser:
    parser = yapx.ArgumentParser(
        prog="rsync",
        description="rsync is a file transfer program capable of efficient remote update via a fast differencing algorithm.",
    )

    # Add the options to the parser
    parser.add_argument("SRC")
    parser.add_argument("DEST")
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="increase verbosity",
    )
    parser.add_argument(
        "--info",
        dest="info_flags",
        metavar="FLAGS",
        help="fine-grained informational verbosity",
    )
    parser.add_argument(
        "--debug",
        dest="debug_flags",
        metavar="FLAGS",
        help="fine-grained debug verbosity",
    )
    parser.add_argument(
        "--stderr",
        choices=["e", "a", "c"],
        default="c",
        help="change stderr output mode (default: errors)",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="suppress non-error messages",
    )
    parser.add_argument(
        "--no-motd",
        action="store_true",
        help="suppress daemon-mode MOTD",
    )
    parser.add_argument(
        "--checksum",
        "-c",
        action="store_true",
        help="skip based on checksum, not mod-time & size",
    )
    parser.add_argument(
        "--archive",
        "-a",
        action="store_true",
        help="archive mode is -rlptgoD (no -A,-X,-U,-N,-H)",
    )
    parser.add_argument(
        "--no-OPTION",
        dest="no_options",
        metavar="OPTION",
        help="turn off an implied OPTION (e.g. --no-D)",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="recurse into directories",
    )
    parser.add_argument(
        "--relative",
        "-R",
        action="store_true",
        help="use relative path names",
    )
    parser.add_argument(
        "--no-implied-dirs",
        action="store_true",
        help="don't send implied dirs with --relative",
    )
    parser.add_argument(
        "--backup",
        "-b",
        action="store_true",
        help="make backups (see --suffix & --backup-dir)",
    )
    parser.add_argument(
        "--backup-dir",
        metavar="DIR",
        help="make backups into hierarchy based in DIR",
    )
    parser.add_argument(
        "--suffix",
        metavar="SUFFIX",
        help="backup suffix (default ~ w/o --backup-dir)",
    )
    parser.add_argument(
        "--update",
        "-u",
        action="store_true",
        help="skip files that are newer on the receiver",
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="update destination files in-place",
    )

    return parser


def main():
    invoke_tui(rsync())
