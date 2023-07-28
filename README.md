# TUIview [`tv`]

> A TUI for every CLI.

| Links         |                                          |
|---------------|------------------------------------------|
| Code Repo     | https://www.github.com/fresh2dev/tuiview |
| Mirror Repo   | https://www.f2dv.com/r/tuiview           |
| Documentation | https://www.f2dv.com/r/tuiview           |
| Changelog     | https://www.f2dv.com/r/tuiview/changelog |
| License       | https://www.f2dv.com/r/tuiview/license   |
| Funding       | https://www.f2dv.com/fund                |

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.f2dv.com/r/tuiview/changelog)
[![GitHub Release Date](https://img.shields.io/github/release-date/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.f2dv.com/r/tuiview/changelog)
[![License](https://img.shields.io/github/license/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.f2dv.com/r/tuiview/license)
[![GitHub Repo stars](https://img.shields.io/github/stars/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://star-history.com/#fresh2dev/tuiview&Date)
[![GitHub issues](https://img.shields.io/github/issues-raw/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.github.com/fresh2dev/tuiview/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.github.com/fresh2dev/tuiview/pulls)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tuiview?color=blue&style=for-the-badge)](https://pypi.org/project/tuiview)
[![Docker Pulls](https://img.shields.io/docker/pulls/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://hub.docker.com/r/fresh2dev/tuiview)
[![Changelog](https://img.shields.io/website?down_message=unavailable&label=docs&style=for-the-badge&up_color=blue&up_message=available&url=https://www.f2dv.com/r/tuiview/changelog)](https://www.f2dv.com/r/tuiview/changelog)
[![Funding](https://img.shields.io/badge/funding-%24%24%24-blue?style=for-the-badge)](https://www.f2dv.com/fund)

---

## Overview

`argparse-tui` is a Python library that will display a Textual UI (TUI) given a Python argparse ArgumentParser. With it, Argparse becomes the specification language for your TUI, powered by the [Textualize]() TUI framework.

TUIview is a command-line tool that contains a collection of "equivalent-enough" (and untested) Argparse implementations of common CLI tools.

Turns out, ChatGPT is decent at translating structured help text into a Python argparse ArgumentParser. This project does not use an AI, but what I've done so far is use GPT 3.5 to generate "equivalent-enough" Argparse implementations of `git`, `rsync`, and `grep`. I plan to clean these up some and add more for other great CLI tools like `fd` and `rg`.

## Install

Install using `pipx` (or `pip`):

```
pipx install tuiview
```

## Use

Installing TUIview gives you both `tuiview` and `tv` for short.

```
________________________________________________________________________________

$ tv
________________________________________________________________________________

Helpful Parameters:
  -h, --help            Show this help message.
  --help-all            Show help for all commands.
  --version             Show the program version number.
  --print-shell-completion {bash,zsh,tcsh}
                        Print shell completion script.

Optional Parameters:
  -f, --from-file <value>
                        > Type: Path, Default: None

Commands:
  <COMMAND>
    git
    rsync
    grep
```

### Built-in Tools

Launch the TUI of a known tool by providing its name:

```
tv git
```

```
tv rsync
```

...

Notice how `git` has subcommands (`commit`, `merge`, ...). The TUI can be limited to a specific command by giving its name:

```
tv git commit
```

### Load from File

Recall that argparse-tui allows us to use argparse as a specification language for Textual UIs. So, given a file defining and populating an argparse ArgumentParser with the variable name `parser`, you can feed it into `tuiview` and view the tui, dude :metal:

For example, save the following to `echo.py`:

```python
import argparse

parser = argparse.ArgumentParser(prog="echo")

parser.add_argument("text", nargs="*")

parser.add_argument(
    "-n",
    action="store_true",
    help="do not output the trailing newline",
)
```

> Hint: see this, and `ping.py` in the `examples/` folder

Now display the TUI using: `tv -f echo.py`

## Contribute

If you think this is as cool as I do and want to contribute and help curate files of argparse parsers for various CLI tools, rock on :metal:

## Support

If this project delivers value to you, please [provide feedback](https://www.github.com/fresh2dev/tuiview/issues), code contributions, and/or [funding](https://www.f2dv.com/fund).

*Brought to you by...*

<a href="https://www.f2dv.com"><img src="https://img.fresh2.dev/fresh2dev.svg" style="filter: invert(50%);"></img></a>
