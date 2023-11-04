import argparse
import os
import subprocess as sp
import sys
from contextlib import contextmanager
from importlib import import_module
from pathlib import Path
from shutil import copy, which
from types import ModuleType
from typing import Any, Dict, List, Optional, Tuple, Union

import yapx
from argparse_tui import invoke_tui
from yapx.types import Annotated

from .__version__ import __version__

TV_MODULES: Dict[str, Union[Path, ModuleType]] = {}
TV_MODULE_DIR: Path = (
    Path(os.environ["TV_MODULE_DIR"])
    if os.getenv("TV_MODULE_DIR", None)
    else Path.home() / ".tuiview"
)
TV_MODULE_DIR_INTERNAL: Path = Path(__file__).parent / "cmd"

SUPPORTED_SPEC_FILE_EXTS: Tuple[str, ...] = (".yml", ".yaml", ".json")
SUPPORTED_FILE_EXTS: Tuple[str, ...] = (".py", *SUPPORTED_SPEC_FILE_EXTS)


@contextmanager
def append_to_sys_path(path: Union[str, Path]):
    original_path = sys.path.copy()
    sys.path.append(str(path))

    try:
        yield
    finally:
        sys.path = original_path


def get_parser_from_module(module: ModuleType) -> argparse.ArgumentParser:
    parser_attr: str = "program"
    candidate_attrs: List[str] = [
        parser_attr,
        "parser",
        "tui",
        "cli",
        "form",
        "app",
        "prog",
        "prg",
    ]
    candidate_attrs.extend(x.upper() for x in candidate_attrs.copy())

    for attr in candidate_attrs:
        if hasattr(module, attr):
            parser_attr = attr
            break

    try:
        parser: argparse.ArgumentParser = getattr(module, parser_attr)
    except AttributeError as e:
        err: str = (
            f"None of these attributes found in module:\n{', '.join(candidate_attrs)}"
        )
        raise AttributeError(err) from e

    if not isinstance(parser, argparse.ArgumentParser):
        err: str = f"The value of '{parser_attr}' is not an argparse.ArgumentParser"
        raise TypeError(err)

    return parser


def import_modules_from_package(
    name: Optional[str] = None,
) -> Dict[str, Union[Path, ModuleType]]:
    supported_files: List[Path] = [
        y
        for x in SUPPORTED_FILE_EXTS
        for y in TV_MODULE_DIR_INTERNAL.glob(f"*{x}")
        if not y.name.startswith("_")
    ]

    return {
        prog_name: (
            x
            if x.suffix in SUPPORTED_SPEC_FILE_EXTS
            else import_module(f".{x.parent.stem}.{x.stem}", package=__package__)
        )
        for x in sorted(supported_files)
        for prog_name in [to_prog_name(x.stem)]
        if name is None or prog_name == name
    }


def import_module_from_file(path: Path) -> ModuleType:
    with append_to_sys_path(path.parent):
        return import_module(path.stem)


def import_modules_from_path(
    path: Path,
    name: Optional[str] = None,
) -> Dict[str, Union[Path, ModuleType]]:
    supported_files: List[Path] = [
        y
        for x in SUPPORTED_FILE_EXTS
        for y in path.glob(f"*{x}")
        if not y.name.startswith("_")
    ]

    return {
        prog_name: (
            x if x.suffix in SUPPORTED_SPEC_FILE_EXTS else import_module_from_file(x)
        )
        for x in sorted(supported_files)
        for prog_name in [to_prog_name(x.stem)]
        if name is None or prog_name == name
    }


def invoke_tui_from_file(path: Union[str, Path], *args: str):
    path = Path(path)
    if path.suffix.lower() in SUPPORTED_SPEC_FILE_EXTS:
        parser = yapx.build_parser_from_file(path)
    else:
        module = import_module_from_file(path)
        parser = get_parser_from_module(module)
    invoke_tui(parser, cli_args=args)


def to_prog_name(text: str) -> str:
    return text.split(".")[-1].strip(" _").replace("_", "-").replace(" ", "-")


def is_builtin_module(module: Union[Path, ModuleType]) -> bool:
    return (
        str(module).startswith(str(Path(__file__).parent))
        if isinstance(module, Path)
        else module.__name__.split(".", 1)[0] == __package__
    )


def is_prog_available(name: str) -> bool:
    if which(name):
        return True

    interactive_shell_cmd: List[str] = []

    while True:
        try:
            sp.run(
                [*interactive_shell_cmd, f"type {name}"],
                shell=not interactive_shell_cmd,
                stdout=sp.DEVNULL,
                check=True,
            )
            return True
        except sp.CalledProcessError:
            if interactive_shell_cmd or not os.getenv("SHELL"):
                return False

            # When searching for the command,
            # use an interactive shell as the fallback option.
            interactive_shell_cmd = [os.environ["SHELL"], "-i", "-c"]
        else:
            return True


def import_program(path: Path, force: bool) -> Path:
    TV_MODULE_DIR.mkdir(exist_ok=True)
    tgt_file: Path = TV_MODULE_DIR / path.name
    if not force and tgt_file.exists():
        raise FileExistsError(tgt_file)
    copy(path, tgt_file)
    return tgt_file


class EditProgramAction(argparse.Action):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Any,
        option_string: Optional[str] = None,
    ):
        prog_path: Path = TV_MODULE_DIR

        prog_name: Optional[str] = values
        module: Union[
            None,
            Union[Path, ModuleType],
            List[Union[Path, ModuleType]],
        ] = None

        if prog_name:
            module = [
                module for name, module in TV_MODULES.items() if name == prog_name
            ]

            if not module:
                err: str = f"Program not found: {prog_name}"
                raise ValueError(err)

            assert isinstance(module, list)
            module = module[0]

            if is_builtin_module(module):
                if isinstance(module, Path):
                    prog_path = import_program(module, force=False)
                else:
                    prog_path = import_program(Path(module.__file__), force=False)
            elif isinstance(module, Path):
                prog_path = module
            else:
                prog_path = Path(module.__file__)

        editor: str = os.getenv("EDITOR", "vim")
        sp.run([editor, prog_path], check=False)


def setup(
    list_modules: Annotated[
        bool,
        yapx.arg("l", "list", default=False, help="List all programs."),
    ],
    _edit_program: Annotated[
        Optional[str],
        yapx.arg(
            "e",
            "edit",
            default=None,
            metavar="<program>",
            nargs="?",
            action=EditProgramAction,
            help="Open a program file for editing.",
        ),
    ],
    import_program_file: Annotated[
        Optional[Path],
        yapx.arg(
            "i",
            "import",
            default=None,
            metavar="<file>",
            help="Import a program to make it globally available in TUIview.",
        ),
    ],
    import_force: Annotated[
        Optional[bool],
        yapx.arg(
            "f",
            "force",
            default=False,
            help="On import, overwrite any existing program file.",
        ),
    ],
) -> None:
    if list_modules:
        print()
        print("------------")
        print("- PROVIDED -")
        print("------------")
        any_imported: bool = False
        any_missing: bool = False
        for name, module in TV_MODULES.items():
            if not is_prog_available(name):
                name += " *"
                any_missing = True

            if is_builtin_module(module):
                print(name)
            else:
                if not any_imported:
                    print()
                    print("------------")
                    print("- IMPORTED -")
                    print("------------")
                    any_imported = True
                print(name)

        if any_missing:
            print("\n* = command not found")

    if import_program_file is not None:
        program_copy: Path = import_program(
            import_program_file,
            force=bool(import_force),
        )
        print(f"Successfully imported to: {program_copy}")


def main() -> None:
    first_arg: Optional[str] = (
        sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    )

    if first_arg and first_arg.lower().endswith(SUPPORTED_FILE_EXTS):
        try:
            path: Path = Path(first_arg)
            extra_args: List[str] = sys.argv[2:]
            invoke_tui_from_file(path, *extra_args)
        except FileNotFoundError as e:
            print("File not found:", e)
        except (AttributeError, TypeError) as e:
            print(e)

        return

    prog_filter: Optional[str] = first_arg
    while not TV_MODULES:
        TV_MODULES.update(import_modules_from_package(name=prog_filter))

        if TV_MODULE_DIR.exists():
            for k, v in import_modules_from_path(TV_MODULE_DIR, name=first_arg).items():
                # delete, then re-add to maintain order.
                if k in TV_MODULES:
                    del TV_MODULES[k]
                TV_MODULES[k] = v

        # if there is a filter and no modules are found,
        # remove the filter and loop again to retrieve all modules.

        if prog_filter is None:
            break
        prog_filter = None

    subcommands: List[yapx.Command] = []
    for prog_name, module in TV_MODULES.items():
        _this_parser: argparse.ArgumentParser = (
            yapx.build_parser_from_file(module)
            if isinstance(module, Path)
            else get_parser_from_module(module)
        )

        argparse_default_prog: str = Path(sys.argv[0]).stem
        if not _this_parser.prog or _this_parser.prog == argparse_default_prog:
            _this_parser.prog = prog_name
        elif _this_parser.prog.lower() != prog_name:
            err: str = f"The base name of the file should be equal to the name of the program: {prog_name} != {_this_parser.prog}"
            raise ValueError(err)
        elif is_prog_available(prog_name):

            def _invoke_tui_from_this_parser(*args: str, _parser=_this_parser):
                invoke_tui(_parser, cli_args=args)

            cmd_help: Optional[str] = (
                _this_parser.description if _this_parser.description else module.__doc__
            )
            if cmd_help:
                _invoke_tui_from_this_parser.__doc__ = cmd_help

            subcommands.append(
                yapx.cmd(
                    _invoke_tui_from_this_parser,
                    name=_this_parser.prog,
                    add_help=False,
                ),
            )

    try:
        yapx.run(
            setup,
            subcommands,
            prog_version=__version__,
            args=sys.argv[1:],
            add_help=True,
            add_help_all=False,
            tui_flags=[],
            default_args=["--help"],
        )
    except FileExistsError as e:
        print("File already exists:", e)
