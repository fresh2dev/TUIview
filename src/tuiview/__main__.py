import sys
from importlib import import_module
from pathlib import Path
from typing import Optional

import yapx
from argparse_tui import invoke_tui
from yapx.types import Annotated

from .__version__ import __version__
from .cmd.git import main as git_main
from .cmd.grep import main as grep_main
from .cmd.rsync import main as rsync_main


def setup(
    from_file: Annotated[Optional[Path], yapx.arg(None, flags=["-f", "--from-file"])],
):
    if from_file:
        sys.path.append(str(from_file.parent))
        module = import_module(from_file.stem)

        invoke_tui(module.parser)

        sys.exit(0)


def main() -> None:
    yapx.run(
        setup,
        named_subcommands={
            "git": git_main,
            "rsync": rsync_main,
            "grep": grep_main,
        },
        prog_version=__version__,
        default_args=["--help"],
        tui_flags=[],
    )


if __name__ == "__main__":
    main()
