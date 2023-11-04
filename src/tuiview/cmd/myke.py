import subprocess
import sys
from argparse import ArgumentParser

if len(sys.argv) > 1 and sys.argv[1] == "myke":
    p: subprocess.CompletedProcess = subprocess.run(
        [*sys.argv[1:], "--tui"],
        check=False,
    )
    sys.exit(p.returncode)
else:
    parser = ArgumentParser(
        prog="myke",
        description="The dynamic Python CLI task runner.",
        add_help=False,
    )
