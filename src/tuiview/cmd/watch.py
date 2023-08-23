import argparse

parser = argparse.ArgumentParser(
    prog="watch",
    description="watch command",
    add_help=False,
)

parser.add_argument("command", help="command to watch")
parser.add_argument(
    "-b",
    "--beep",
    action="store_true",
    help="beep if command has a non-zero exit",
)
parser.add_argument(
    "-c",
    "--color",
    action="store_true",
    help="interpret ANSI color and style sequences",
)
parser.add_argument(
    "-d",
    "--differences",
    nargs="?",
    const="<permanent>",
    help="highlight changes between updates",
)
parser.add_argument(
    "-e",
    "--errexit",
    action="store_true",
    help="exit if command has a non-zero exit",
)
parser.add_argument(
    "-g",
    "--chgexit",
    action="store_true",
    help="exit when output from command changes",
)
parser.add_argument(
    "-n",
    "--interval",
    type=int,
    help="seconds to wait between updates",
)
parser.add_argument(
    "-p",
    "--precise",
    action="store_true",
    help="attempt run command in precise intervals",
)
parser.add_argument("-t", "--no-title", action="store_true", help="turn off header")
parser.add_argument(
    "-w",
    "--no-wrap",
    action="store_true",
    help="turn off line wrapping",
)
parser.add_argument(
    "-x",
    "--exec",
    action="store_true",
    help='pass command to exec instead of "sh -c"',
)

parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s 1.0",
    help="output version information and exit",
)
