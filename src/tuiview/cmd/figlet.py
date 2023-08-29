import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="figlet",
    description="display large characters made up of ordinary screen characters",
    add_help=False,
)

# Add the command-line arguments
parser.add_argument("-f", dest="fontfile", help="Select the font")
parser.add_argument(
    "-d",
    dest="fontdirectory",
    help="Change the default font directory",
)
parser.add_argument("-c", action="store_true", help="Center the output horizontally")
parser.add_argument("-l", action="store_true", help="Make the output flush-left")
parser.add_argument("-r", action="store_true", help="Make the output flush-right")
parser.add_argument(
    "-x",
    action="store_true",
    help="Set the justification based on text direction",
)
parser.add_argument(
    "-t",
    action="store_true",
    help="Set the output width to the terminal width",
)
parser.add_argument(
    "-w",
    dest="outputwidth",
    type=int,
    help="Set the output width to the given integer",
)
parser.add_argument("-p", action="store_true", help="Put FIGlet into paragraph mode")
parser.add_argument("-n", action="store_true", help="Put FIGlet back to normal")
parser.add_argument(
    "-D",
    action="store_true",
    help="Switch to the German character set",
)
parser.add_argument("-E", action="store_true", help="Turn off -D processing")
parser.add_argument("-C", dest="controlfile", help="Add the given controlfile")
parser.add_argument("-N", action="store_true", help="Clear the controlfile list")
parser.add_argument(
    "-s",
    action="store_true",
    help="Enable smushing to display FIGcharacters close together",
)
parser.add_argument(
    "-S",
    action="store_true",
    help="Enable smushing with support for kerning or full width",
)
parser.add_argument(
    "-k",
    action="store_true",
    help="Enable kerning between FIGcharacters",
)
parser.add_argument(
    "-W",
    action="store_true",
    help="Display all FIGcharacters at their full width",
)
parser.add_argument(
    "-o",
    action="store_true",
    help="Enable overlapping of FIGcharacters",
)
parser.add_argument(
    "-m",
    dest="layoutmode",
    type=int,
    help="Specify an explicit layoutmode between 1 and 63",
)
parser.add_argument(
    "-v",
    action="version",
    version="%(prog)s version 1.0",
    help="Print version and copyright information",
)
parser.add_argument(
    "-I",
    dest="infocode",
    type=int,
    help="Print information corresponding to the given infocode",
)
parser.add_argument("message", nargs="?", help="Input message")
