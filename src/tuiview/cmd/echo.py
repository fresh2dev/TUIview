import argparse

parser = argparse.ArgumentParser(prog="echo", description="Print text", add_help=False)

parser.add_argument("STRING", nargs="*")

parser.add_argument(
    "-n",
    action="store_true",
    help="do not output the trailing newline",
)
