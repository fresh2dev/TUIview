<h1 align="center">TUIview [<code>tv</code>]</h1>
<p align="center"><em>A TUI for every CLI</em> :tv:</p>
<h2 align="center">
<a href="https://www.f2dv.com/r/tuiview/" target="_blank">Documentation</a>
| <a href="https://www.f2dv.com/s/tuiview/" target="_blank">Slide Deck</a>
| <a href="https://www.github.com/fresh2dev/tuiview/" target="_blank">Git Repo</a>
</h2>

*TUIview* [`tv`] allows you to create Textual User Interfaces (TUIs) for command-line interfaces (CLIs) that do not provide their own TUI.

By prefixing any supported CLI command with the `tv` command -- `tv <program>` -- you can interact with a TUI form to interactively build and execute CLI commands for *\<program>*.

TUIview accepts spec from YAML files, or from Python files that implement an Argparse `ArgumentParser`.

TUIview is a tool for displaying these "programs", and also provides a built-in repository of curated programs.

Care to contribute or improve a TV program? PRs welcome :call_me_hand:

## Install

```
pipx install tuiview
```

or

```
pip install tuiview
```

## Use

<a href="https://www.f2dv.com/s/tuiview/" target="_blank">
    <img src="https://img.fresh2.dev/slides_placeholder.png"></img>
</a>

<video autoplay="false" controls="controls">
  <source src="https://img.fresh2.dev/tv_demo.webm" type="video/webm"/>
  <p><i>This page does not support webm video playback.</i></p>
  <p><i><a href="https://www.f2dv.com/r/tuiview/" target="_blank">Click here to watch a video demo.</a></i></p>
</video>

## Programs

> Legend:
:green_circle: = Verified
:yellow_circle: = Unverified
:white_circle: = ToDo


- :green_circle: pastel

- :yellow_circle: alacritty
- :yellow_circle: cloc
- :yellow_circle: delta
- :yellow_circle: df
- :yellow_circle: diff
- :yellow_circle: du
- :yellow_circle: fd
- :yellow_circle: figlet
- :yellow_circle: git
- :yellow_circle: gping
- :yellow_circle: grep
- :yellow_circle: jq
- :yellow_circle: mods
- :yellow_circle: pandoc
- :yellow_circle: ping
- :yellow_circle: rsync
- :yellow_circle: scc
- :yellow_circle: tree
- :yellow_circle: unzip
- :yellow_circle: watch


- :white_circle: ansible
- :white_circle: asciinema
- :white_circle: bandwhich
- :white_circle: conda
- :white_circle: curl
- :white_circle: curlie
- :white_circle: dig
- :white_circle: docker
- :white_circle: dog
- :white_circle: duf
- :white_circle: dust
- :white_circle: entr
- :white_circle: ffmpeg
- :white_circle: gh
- :white_circle: git-cliff
- :white_circle: grex
- :white_circle: gum
- :white_circle: httpie
- :white_circle: hugo
- :white_circle: hyperfine
- :white_circle: jupyter
- :white_circle: kubectl
- :white_circle: marp
- :white_circle: mkdocs
- :white_circle: ntfy
- :white_circle: ouch
- :white_circle: pip
- :white_circle: pipx
- :white_circle: procs
- :white_circle: pyenv
- :white_circle: pylint
- :white_circle: pytest
- :white_circle: ripgrep
- :white_circle: sd
- :white_circle: ser (servicer)
- :white_circle: tar
- :white_circle: tox
- :white_circle: tre
- :white_circle: vimdiff
- :white_circle: wget
- :white_circle: zoxide

---

[![License](https://img.shields.io/github/license/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.f2dv.com/r/tuiview/license/)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/fresh2dev/tuiview?filter=!*%5Ba-z%5D*&style=for-the-badge&label=Release&color=blue)](https://www.f2dv.com/r/tuiview/changelog/)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/fresh2dev/tuiview/main?style=for-the-badge&label=updated&color=blue)](https://www.f2dv.com/r/tuiview/changelog/)
[![GitHub Repo stars](https://img.shields.io/github/stars/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://star-history.com/#fresh2dev/tuiview&Date)
[![Funding](https://img.shields.io/badge/funding-%24%24%24-blue?style=for-the-badge)](https://www.f2dv.com/fund/)
<!-- [![GitHub issues](https://img.shields.io/github/issues-raw/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.github.com/fresh2dev/tuiview/issues/) -->
<!-- [![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://www.github.com/fresh2dev/tuiview/pulls/) -->
<!-- [![PyPI - Downloads](https://img.shields.io/pypi/dm/tuiview?color=blue&style=for-the-badge)](https://pypi.org/project/tuiview/) -->
<!-- [![Docker Pulls](https://img.shields.io/docker/pulls/fresh2dev/tuiview?color=blue&style=for-the-badge)](https://hub.docker.com/r/fresh2dev/tuiview/) -->
