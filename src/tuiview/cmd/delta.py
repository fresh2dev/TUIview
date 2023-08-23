import argparse

parser = argparse.ArgumentParser(
    prog="delta",
    description="A viewer for git and diff output",
    add_help=False,
)

parser.add_argument(
    "MINUS_FILE",
    metavar="<MINUS_FILE>",
    type=str,
    help="First file to be compared when delta is being used in diff mode",
)
parser.add_argument(
    "PLUS_FILE",
    metavar="<PLUS_FILE>",
    type=str,
    help="Second file to be compared when delta is being used in diff mode",
)

parser.add_argument(
    "--blame-code-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for the code section of a git blame line",
)
parser.add_argument(
    "--blame-format",
    metavar="<FMT>",
    type=str,
    default="{timestamp:<15} {author:<15.14} {commit:<8}",
    help='Format string for git blame commit metadata [default: "{timestamp:<15} {author:<15.14} {commit:<8}"]',
)
parser.add_argument(
    "--blame-palette",
    metavar="<COLORS>",
    type=str,
    help="Background colors used for git blame lines (space-separated string)",
)
parser.add_argument(
    "--blame-separator-format",
    metavar="<FMT>",
    type=str,
    default="│{n:^4}│",
    help="Separator between the blame format and the code section of a git blame line [default: │{n:^4}│]",
)
parser.add_argument(
    "--blame-separator-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for the blame-separator-format",
)
parser.add_argument(
    "--blame-timestamp-format",
    metavar="<FMT>",
    type=str,
    default="%Y-%m-%d %H:%M:%S %z",
    help='Format of `git blame` timestamp in raw git output received by delta [default: "%Y-%m-%d %H:%M:%S %z"]',
)
parser.add_argument(
    "--blame-timestamp-output-format",
    metavar="<FMT>",
    type=str,
    help="Format string for git blame timestamp output",
)
parser.add_argument(
    "--color-only",
    action="store_true",
    help="Do not alter the input structurally in any way",
)
parser.add_argument(
    "--commit-decoration-style",
    metavar="<STYLE>",
    type=str,
    default="",
    help="Style string for the commit hash decoration [default: ]",
)
parser.add_argument(
    "--commit-regex",
    metavar="<REGEX>",
    type=str,
    default="^commit ",
    help='Regular expression used to identify the commit line when parsing git output [default: "^commit "]',
)
parser.add_argument(
    "--commit-style",
    metavar="<STYLE>",
    type=str,
    default="raw",
    help="Style string for the commit hash line [default: raw]",
)
parser.add_argument(
    "--dark",
    action="store_true",
    help="Use default colors appropriate for a dark terminal background",
)
parser.add_argument(
    "--default-language",
    metavar="<LANG>",
    type=str,
    help="Default language used for syntax highlighting",
)
parser.add_argument(
    "--diff-highlight",
    action="store_true",
    help="Emulate diff-highlight",
)
parser.add_argument(
    "--diff-so-fancy",
    action="store_true",
    help="Emulate diff-so-fancy",
)
parser.add_argument(
    "--diff-stat-align-width",
    metavar="<N>",
    type=int,
    default=48,
    help="Width allocated for file paths in a diff stat section [default: 48]",
)
parser.add_argument(
    "--features",
    metavar="<FEATURES>",
    type=str,
    help="Names of delta features to activate (space-separated)",
)
parser.add_argument(
    "--file-added-label",
    metavar="<STRING>",
    type=str,
    default="added:",
    help="Text to display before an added file path [default: added:]",
)
parser.add_argument(
    "--file-copied-label",
    metavar="<STRING>",
    type=str,
    default="copied:",
    help="Text to display before a copied file path [default: copied:]",
)
parser.add_argument(
    "--file-decoration-style",
    metavar="<STYLE>",
    type=str,
    default="blue ul",
    help='Style string for the file decoration [default: "blue ul"]',
)
parser.add_argument(
    "--file-modified-label",
    metavar="<STRING>",
    type=str,
    default="",
    help="Text to display before a modified file path [default: ]",
)
parser.add_argument(
    "--file-removed-label",
    metavar="<STRING>",
    type=str,
    default="removed:",
    help="Text to display before a removed file path [default: removed:]",
)
parser.add_argument(
    "--file-renamed-label",
    metavar="<STRING>",
    type=str,
    default="renamed:",
    help="Text to display before a renamed file path [default: renamed:]",
)
parser.add_argument(
    "--file-style",
    metavar="<STYLE>",
    type=str,
    default="blue",
    help="Style string for the file section [default: blue]",
)
parser.add_argument(
    "--file-transformation",
    metavar="<SED_CMD>",
    type=str,
    help="Sed-style command transforming file paths for display",
)
parser.add_argument(
    "--grep-context-line-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for non-matching lines of grep output",
)
parser.add_argument(
    "--grep-file-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for file paths in grep output",
)
parser.add_argument(
    "--grep-line-number-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for line numbers in grep output",
)
parser.add_argument(
    "--grep-match-line-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for matching lines of grep output",
)
parser.add_argument(
    "--grep-match-word-style",
    metavar="<STYLE>",
    type=str,
    help="Style string for the matching substrings within a matching line of grep output",
)
parser.add_argument(
    "--grep-separator-symbol",
    metavar="<STRING>",
    type=str,
    default=":",
    help="Separator symbol printed after the file path and line number in grep output [default: :]",
)
parser.add_argument(
    "--hunk-header-decoration-style",
    metavar="<STYLE>",
    type=str,
    default="blue box",
    help='Style string for the hunk-header decoration [default: "blue box"]',
)
parser.add_argument(
    "--hunk-header-file-style",
    metavar="<STYLE>",
    type=str,
    default="blue",
    help="Style string for the file path part of the hunk-header [default: blue]",
)
parser.add_argument(
    "--hunk-header-line-number-style",
    metavar="<STYLE>",
    type=str,
    default="blue",
    help="Style string for the line number part of the hunk-header [default: blue]",
)
parser.add_argument(
    "--hunk-header-style",
    metavar="<STYLE>",
    type=str,
    default="line-number syntax",
    help='Style string for the hunk-header [default: "line-number syntax"]',
)
parser.add_argument(
    "--hunk-label",
    metavar="<STRING>",
    type=str,
    default="",
    help="Text to display before a hunk header [default: ]",
)
parser.add_argument(
    "--hyperlinks",
    action="store_true",
    help="Render commit hashes, file names, and line numbers as hyperlinks",
)
parser.add_argument(
    "--hyperlinks-commit-link-format",
    metavar="<FMT>",
    type=str,
    help="Format string for commit hyperlinks (requires --hyperlinks)",
)
parser.add_argument(
    "--hyperlinks-file-link-format",
    metavar="<FMT>",
    type=str,
    default="file://{path}",
    help="Format string for file hyperlinks (requires --hyperlinks) [default: file://{path}]",
)
parser.add_argument(
    "--inline-hint-style",
    metavar="<STYLE>",
    type=str,
    default="blue",
    help="Style string for short inline hint text [default: blue]",
)
parser.add_argument(
    "--inspect-raw-lines",
    metavar="<true|false>",
    type=bool,
    default=True,
    help="Kill-switch for --color-moved support [default: true]",
)
parser.add_argument(
    "--keep-plus-minus-markers",
    action="store_true",
    help="Prefix added/removed lines with a +/- character, as git does",
)
parser.add_argument(
    "--light",
    action="store_true",
    help="Use default colors appropriate for a light terminal background",
)
parser.add_argument(
    "--line-buffer-size",
    metavar="<N>",
    type=int,
    default=32,
    help="Size of internal line buffer [default: 32]",
)
parser.add_argument(
    "--line-fill-method",
    metavar="<STRING>",
    type=str,
    help="Line-fill method in side-by-side mode",
)
parser.add_argument(
    "-n",
    "--line-numbers",
    action="store_true",
    help="Display line numbers next to the diff",
)
parser.add_argument(
    "--line-numbers-left-format",
    metavar="<FMT>",
    type=str,
    default="{nm:^4}⋮",
    help="Format string for the left column of line numbers [default: {nm:^4}⋮]",
)
