import argparse

# Create the main parser
parser = argparse.ArgumentParser(
    prog="alacritty",
    description="A fast, cross-platform, OpenGL terminal emulator",
    usage="%(prog)s [OPTIONS] [SUBCOMMAND]",
    add_help=False,
)

# Add options
parser.add_argument(
    "-e",
    "--command",
    nargs=argparse.REMAINDER,
    metavar="<COMMAND>",
    help="Command and args to execute (must be last argument)",
)
parser.add_argument(
    "--working-directory",
    metavar="<WORKING_DIRECTORY>",
    help="Start the shell in the specified working directory",
)
parser.add_argument(
    "-t",
    "--title",
    metavar="<TITLE>",
    default="Alacritty",
    help="Defines the window title [default: Alacritty]",
)
parser.add_argument(
    "--config-file",
    metavar="<CONFIG_FILE>",
    help="Specify alternative configuration file [default: $XDG_CONFIG_HOME/alacritty/alacritty.yml]",
)
parser.add_argument(
    "--embed",
    metavar="<EMBED>",
    help="X11 window ID to embed Alacritty within (decimal or hexadecimal with '0x' prefix)",
)
parser.add_argument(
    "--hold",
    action="store_true",
    help="Remain open after child process exit",
)
parser.add_argument(
    "--class",
    dest="window_class",
    metavar="<instance> | <instance>,<general>",
    help="Defines window class/app_id on X11/Wayland [default: Alacritty]",
)
parser.add_argument(
    "--print-events",
    action="store_true",
    help="Print all events to stdout",
)
parser.add_argument("--ref-test", action="store_true", help="Generates ref test")
parser.add_argument(
    "-v",
    action="count",
    default=0,
    help="Increases the level of verbosity (the max level is -vvv)",
)
parser.add_argument(
    "-q",
    action="count",
    default=0,
    help="Reduces the level of verbosity (the min level is -qq)",
)
parser.add_argument(
    "-V",
    "--version",
    action="store_true",
    help="Print version information",
)
