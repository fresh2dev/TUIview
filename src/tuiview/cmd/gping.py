import argparse

parser = argparse.ArgumentParser(
    prog="gping",
    description="Ping, but with a graph.",
    add_help=False,
)

# Add arguments
parser.add_argument(
    "hosts_or_commands",
    nargs=argparse.REMAINDER,
    help="Hosts or IPs to ping, or commands to run if --cmd is provided. Can use cloud shorthands like aws:eu-west-1.",
)
parser.add_argument(
    "--cmd",
    action="store_true",
    help="Graph the execution time for a list of commands rather than pinging hosts",
)
parser.add_argument(
    "-n",
    "--watch-interval",
    metavar="WATCH_INTERVAL",
    help="Watch interval seconds (provide partial seconds like '0.5'). Default for ping is 0.2, default for cmd is 0.5.",
)
parser.add_argument(
    "-b",
    "--buffer",
    metavar="BUFFER",
    default="30",
    help="Determines the number of seconds to display in the graph. [default: 30]",
)
parser.add_argument(
    "-4",
    action="store_true",
    help="Resolve ping targets to IPv4 address",
)
parser.add_argument(
    "-6",
    action="store_true",
    help="Resolve ping targets to IPv6 address",
)
parser.add_argument(
    "-i",
    "--interface",
    metavar="INTERFACE",
    help="Interface to use when pinging",
)
parser.add_argument(
    "-s",
    "--simple-graphics",
    action="store_true",
    help="Uses dot characters instead of braille",
)
parser.add_argument(
    "--vertical-margin",
    metavar="VERTICAL_MARGIN",
    default="1",
    help="Vertical margin around the graph (top and bottom) [default: 1]",
)
parser.add_argument(
    "--horizontal-margin",
    metavar="HORIZONTAL_MARGIN",
    default="0",
    help="Horizontal margin around the graph (left and right) [default: 0]",
)
parser.add_argument(
    "-c",
    "--color",
    metavar="color",
    action="append",
    help="Assign color to a graph entry. This option can be defined more than once as a comma separated string, and the order which the colors are provided will be matched against the hosts or commands passed to gping. Hexadecimal RGB color codes are accepted in the form of '#RRGGBB' or the following color names: 'black', 'red', 'green', 'yellow', 'blue', 'magenta','cyan', 'gray', 'dark-gray', 'light-red', 'light-green', 'light-yellow', 'light-blue', 'light-magenta', 'light-cyan', and 'white'",
)
parser.add_argument(
    "--clear",
    action="store_true",
    help="Clear the graph from the terminal after closing the program",
)
parser.add_argument(
    "-V",
    "--version",
    action="version",
    version="%(prog)s 1.0",
    help="Print version",
)
