import yapx
from argparse_tui import invoke_tui


def grep() -> yapx.ArgumentParser:
    parser = yapx.ArgumentParser(
        prog="grep",
        description="Search for PATTERNS in each FILE.",
    )

    # Usage information
    parser.add_argument(
        "patterns",
        metavar="PATTERNS",
        type=str,
        nargs="+",
        help="patterns to search for",
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        type=str,
        nargs="*",
        default=["**"],
        help="files to search in",
    )

    # Pattern selection and interpretation
    group = parser.add_argument_group(title="Pattern selection and interpretation")
    group.add_argument(
        "-E",
        "--extended-regexp",
        action="store_true",
        help="PATTERNS are extended regular expressions",
    )
    group.add_argument(
        "-F",
        "--fixed-strings",
        action="store_true",
        help="PATTERNS are strings",
    )
    group.add_argument(
        "-G",
        "--basic-regexp",
        action="store_true",
        help="PATTERNS are basic regular expressions",
    )
    group.add_argument(
        "-P",
        "--perl-regexp",
        action="store_true",
        help="PATTERNS are Perl regular expressions",
    )

    # Case sensitivity
    parser.add_argument(
        "--ignore-case / --no-ignore-case",
        action=yapx.actions.BooleanOptionalAction,
        help="ignore case distinctions in patterns and data",
        default=False,
    )

    # Pattern matching options
    group = parser.add_argument_group(title="Pattern matching options")
    group.add_argument(
        "-w",
        "--word-regexp",
        action="store_true",
        help="match only whole words",
    )
    group.add_argument(
        "-x",
        "--line-regexp",
        action="store_true",
        help="match only whole lines",
    )
    group.add_argument(
        "-z",
        "--null-data",
        action="store_true",
        help="a data line ends in 0 byte, not newline",
    )

    # Miscellaneous options
    group = parser.add_argument_group(title="Miscellaneous options")
    group.add_argument(
        "-s",
        "--no-messages",
        action="store_true",
        help="suppress error messages",
    )
    group.add_argument(
        "-v",
        "--invert-match",
        action="store_true",
        help="select non-matching lines",
    )
    group.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="display version information and exit",
    )

    # Output control options
    group = parser.add_argument_group(title="Output control options")
    group.add_argument(
        "-m",
        "--max-count",
        metavar="NUM",
        type=int,
        help="stop after NUM selected lines",
    )
    group.add_argument(
        "-b",
        "--byte-offset",
        action="store_true",
        help="print the byte offset with output lines",
    )
    group.add_argument(
        "-n",
        "--line-number",
        action="store_true",
        help="print line number with output lines",
    )

    return parser


def main():
    invoke_tui(grep())
