import os
import sys
from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
from typing import Any, Callable, Dict, List

import yapx
from argparse_tui import invoke_tui

from .__version__ import __version__


def invoke_tui_from_file(path: Path, *args):
    if not path.exists():
        raise FileNotFoundError(path)
    sys.path.append(str(path.parent))
    module = import_module(path.stem)
    candidate_attrs: List[str] = ["parser", "tui", "form", "cli", "app"]
    parser_attr: str = candidate_attrs[0]
    for attr in candidate_attrs:
        if hasattr(module, attr):
            parser_attr = attr
            break

    parser: ArgumentParser = getattr(module, parser_attr)
    if not isinstance(parser, ArgumentParser):
        err: str = f"The value of '{parser_attr}' is not an argparse.ArgumentParser"
        raise TypeError(err)

    invoke_tui(module.parser, cli_args=args)


def main() -> None:
    named_subcommands: Dict[str, Callable[..., Any]] = {}

    for x in (Path(__file__).parent / "cmd").glob("*.py"):
        if not x.name.startswith("_"):
            cmd_module = import_module(
                f".{x.parent.stem}.{x.stem}",
                package=__package__,
            )
            named_subcommands[x.stem.replace("_", "-")] = cmd_module.main

    if sys.argv and ("." in sys.argv[1] or os.sep in sys.argv[1]):
        try:
            invoke_tui_from_file(Path(sys.argv[1]), *sys.argv[2:])
        except FileNotFoundError as e:
            print("File not found:", e)
        except (AttributeError, TypeError) as e:
            print(e)
    else:
        yapx.run_commands(
            named_subcommands=named_subcommands,
            prog_version=__version__,
            default_args=["--help"],
            tui_flags=[],
        )
