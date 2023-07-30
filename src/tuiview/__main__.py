import sys
from importlib import import_module
from pathlib import Path
from typing import Any, Callable, Dict

import yapx
from argparse_tui import invoke_tui
from yapx.types import Annotated

from .__version__ import __version__


def from_file(*args, path: Annotated[Path, yapx.arg(pos=True)]):
    sys.path.append(str(path.parent))
    module = import_module(path.stem)

    invoke_tui(module.parser, cli_args=args)

    sys.exit(0)


def main() -> None:
    named_subcommands: Dict[str, Callable[..., Any]] = {}

    for x in (Path(__file__).parent / "cmd").glob("*.py"):
        if not x.name.startswith("_"):
            cmd_module = import_module(
                f".{x.parent.stem}.{x.stem}",
                package=__package__,
            )
            named_subcommands[x.stem.replace("_", "-")] = cmd_module.main

    yapx.run_commands(
        [from_file],
        named_subcommands=named_subcommands,
        prog_version=__version__,
        default_args=["--help"],
        tui_flags=[],
    )


if __name__ == "__main__":
    main()
