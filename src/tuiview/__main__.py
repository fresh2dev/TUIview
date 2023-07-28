import sys
from importlib import import_module
from pathlib import Path
from typing import Any, Callable, Dict, Optional

import yapx
from argparse_tui import invoke_tui
from yapx.types import Annotated

from .__version__ import __version__


def setup(
    from_file: Annotated[Optional[Path], yapx.arg(None, flags=["-f", "--from-file"])],
):
    if from_file:
        sys.path.append(str(from_file.parent))
        module = import_module(from_file.stem)

        invoke_tui(module.parser)

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

    yapx.run(
        setup,
        named_subcommands=named_subcommands,
        prog_version=__version__,
        default_args=["--help"],
        tui_flags=[],
    )


if __name__ == "__main__":
    main()
