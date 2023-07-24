import argparse
from typing import Optional

import yapx
from argparse_tui import invoke_tui
from yapx.types import Annotated


def git_commit(parser):
    parser.prog = "git-commit"
    parser.description = "Record changes to the repository"

    # Add arguments
    parser.add_argument(
        "-m",
        "--message",
        metavar="<msg>",
        action="append",
        help="Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        default=False,
        help="Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.",
    )
    parser.add_argument(
        "--fixup",
        metavar="[(amend|reword):]<commit>",
    )
    parser.add_argument(
        "--squash",
        metavar="<commit>",
    )
    parser.add_argument(
        "-n",
        "--no-verify",
        action="store_true",
        default=False,
        help="By default, the pre-commit and commit-msg hooks are run. When any of --no-verify or -n is given, these are bypassed. See also githooks(5).",
    )
    parser.add_argument(
        "--author",
        metavar="<author>",
        help="Override the commit author. Specify an explicit author using the standard A U Thor <author@example.com> format. Otherwise <author> is assumed to be a pattern and is used to search for an existing commit by that author (i.e. rev-list --all -i --author=<author>); the commit author is then copied from the first such commit found.",
    )
    parser.add_argument(
        "--date",
        metavar="<date>",
        help="Override the author date used in the commit.",
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        default=False,
        help="Usually recording a commit that has the exact same tree as its sole parent commit is a mistake, and the command prevents you from making such a commit. This option bypasses the safety, and is primarily for use by foreign SCM interface scripts.",
    )
    parser.add_argument(
        "-e",
        "--edit",
        action="store_true",
        default=False,
        help="The message taken from file with -F, command line with -m, and from commit object with -C are usually used as the commit log message unmodified. This option lets you further edit the message taken from these sources.",
    )
    parser.add_argument(
        "--no-edit",
        action="store_true",
        default=False,
        help="Use the selected commit message without launching an editor. For example, git commit --amend --no-edit amends a commit without changing its commit message.",
    )
    parser.add_argument(
        "--amend",
        action="store_true",
        default=False,
        help='Replace the tip of the current branch by creating a new commit. The recorded tree is prepared as usual (including the effect of the -i and -o options and explicit pathspec), and the message from the original commit is used as the starting point, instead of an empty message, when no other message is specified from the command line via options such as -m, -F, -c, etc. The new commit has the same parents and author as the current one (the --reset-author option can countermand this). It is a rough equivalent for: $ git reset --soft HEAD^ $ ... do something else to come up with the right tree ... $ git commit -c ORIG_HEAD but can be used to amend a merge commit. You should understand the implications of rewriting history if you amend a commit that has already been published. (See the "RECOVERING FROM UPSTREAM REBASE" section in git-rebase(1).)',
    )
    parser.add_argument(
        "--no-post-rewrite",
        action="store_true",
        default=False,
        help="Bypass the post-rewrite hook.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        default=False,
        help="Suppress commit summary message.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Do not create a commit, but show a list of paths that are to be committed, paths with local changes that will be left uncommitted and paths that are untracked.",
    )


def git_merge(parser):
    parser.prog = "git-merge"
    parser.description = "Join two or more development histories together"

    parser.add_argument("commit", nargs="*", help="Commits to merge into our branch")

    parser.add_argument(
        "-n",
        "--no-commit",
        action="store_true",
        help="Perform the merge without committing the result",
    )
    parser.add_argument(
        "--squash",
        action="store_true",
        help="Produce the working tree and index state as if a real merge happened, but do not actually make a commit",
    )
    parser.add_argument(
        "--stat",
        action="store_true",
        help="Show a diffstat at the end of the merge",
    )
    parser.add_argument(
        "--no-edit",
        dest="edit",
        action="store_true",
        help="Invoke an editor before committing successful mechanical merge",
    )
    parser.add_argument(
        "--no-verify",
        dest="verify",
        action="store_true",
        help="Skip pre-merge and commit-msg hooks",
    )
    parser.add_argument(
        "--verify-signatures",
        dest="verify_signatures",
        action="store_true",
        help="Verify that the tip commit of the side branch being merged is signed with a valid key",
    )
    parser.add_argument("--quiet", "-q", action="store_true", help="Operate quietly")
    parser.add_argument("--verbose", "-v", action="store_true", help="Be verbose")
    parser.add_argument(
        "--progress",
        action=yapx.actions.BooleanOptionalAction,
        help="Turn progress on",
        default=False,
    )
    parser.add_argument(
        "--autostash",
        action="store_true",
        help="Automatically create a temporary stash entry before the operation begins",
    )


def git_log(parser):
    parser.prog = "git-log"
    parser.description = "Show commit logs"

    parser.add_argument(
        "--graph",
        action="store_true",
        help="Draw a text-based graphical representation of the commit history on the left hand side of the output",
    )
    parser.add_argument(
        "--follow",
        action="store_true",
        help="Continue listing the history of a file beyond renames (works only for a single file)",
    )
    parser.add_argument(
        "--decorate",
        nargs="?",
        choices=["short", "full", "auto", "no"],
        const="short",
        help="Print out the ref names of any commits that are shown",
    )
    parser.add_argument(
        "--no-decorate",
        dest="decorate",
        action="store_true",
        help="Print out the ref names of any commits that are shown",
    )
    parser.add_argument(
        "--decorate-refs",
        dest="decorate_refs",
        help="If no --decorate-refs is given, pretend as if all refs were included",
    )
    parser.add_argument(
        "--decorate-refs-exclude",
        dest="decorate_refs_exclude",
        help="If no --decorate-refs is given, pretend as if all refs were included",
    )
    parser.add_argument(
        "--source",
        action="store_true",
        help="Print out the ref name given on the command line by which each commit was reached",
    )
    parser.add_argument(
        "--full-diff",
        action="store_true",
        help='Without this flag, git log -p <path>... shows commits that touch the specified paths, and diffs about the same specified paths. With this, the full diff is shown for commits that touch the specified paths; this means that "<path>..." limits only commits, and doesn’t limit diff for those commits',
    )
    parser.add_argument(
        "-n",
        type=int,
        dest="max_count",
        help="Limit the number of commits to output",
    )
    parser.add_argument(
        "--skip",
        type=int,
        help="Skip number commits before starting to show the commit output",
    )
    parser.add_argument(
        "--since",
        "--after",
        dest="since_date",
        help="Show commits more recent than a specific date",
    )
    parser.add_argument(
        "--until",
        "--before",
        dest="until_date",
        help="Show commits older than a specific date",
    )
    parser.add_argument(
        "--author",
        nargs="+",
        help="Limit the commits output to ones with author header lines that match the specified pattern (regular expression)",
    )
    parser.add_argument(
        "--committer",
        nargs="+",
        help="Limit the commits output to ones with committer header lines that match the specified pattern (regular expression)",
    )
    parser.add_argument(
        "--grep-reflog",
        nargs="+",
        help="Limit the commits output to ones with reflog entries that match the specified pattern (regular expression). It is an error to use this option unless --walk-reflogs is in use",
    )
    parser.add_argument(
        "--grep",
        nargs="+",
        help="Limit the commits output to ones with log message that matches the specified pattern (regular expression). When --notes is in effect, the message from the notes is matched as if it were part of the log message",
    )
    parser.add_argument(
        "--all-match",
        action="store_true",
        help="Limit the commits output to ones that match all given --grep, instead of ones that match at least one",
    )
    parser.add_argument(
        "--invert-grep",
        action="store_true",
        help="Limit the commits output to ones with log message that do not match the pattern specified with --grep",
    )
    parser.add_argument(
        "-i",
        "--regexp-ignore-case",
        action="store_true",
        help="Match the regular expression limiting patterns without regard to letter case",
    )
    parser.add_argument(
        "--basic-regexp",
        action="store_true",
        help="Consider the limiting patterns to be basic regular expressions; this is the default",
    )
    parser.add_argument(
        "-E",
        "--extended-regexp",
        action="store_true",
        help="Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions",
    )
    parser.add_argument(
        "-F",
        "--fixed-strings",
        action="store_true",
        help="Consider the limiting patterns to be fixed strings (don’t interpret pattern as a regular expression)",
    )
    parser.add_argument(
        "-P",
        "--perl-regexp",
        action="store_true",
        help="Consider the limiting patterns to be Perl-compatible regular expressions",
    )
    parser.add_argument(
        "--merges",
        action="store_true",
        help="Print only merge commits. This is exactly the same as --min-parents=2",
    )
    parser.add_argument(
        "--no-merges",
        action="store_true",
        help="Do not print commits with more than one parent. This is exactly the same as --max-parents=1",
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        help="Do not include refs matching <glob-pattern> that the next --all, --branches, --tags, --remotes, or --glob would otherwise consider. Repetitions of this option accumulate exclusion patterns up to the next --all, --branches, --tags, --remotes, or --glob option",
    )
    parser.add_argument(
        "--date-order",
        action="store_true",
        help="Show no parents before all of its children are shown, but otherwise show commits in the commit timestamp order",
    )
    parser.add_argument(
        "--author-date-order",
        action="store_true",
        help="Show no parents before all of its children are shown, but otherwise show commits in the author timestamp order",
    )
    parser.add_argument(
        "--topo-order",
        action="store_true",
        help="Show no parents before all of its children are shown, and avoid showing commits on multiple lines of history intermixed",
    )
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Output the commits chosen to be shown in reverse order. Cannot be combined with --walk-reflogs",
    )
    parser.add_argument(
        "--pretty",
        nargs="?",
        const="format:%H",
        help="Pretty-print the contents of the commit logs in a given format",
    )
    parser.add_argument(
        "--abbrev-commit",
        action="store_true",
        help="Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely",
    )
    parser.add_argument("--no-abbrev-commit", action="store_true")
    parser.add_argument(
        "--oneline",
        action="store_true",
        help='Shorthand for "--pretty=oneline --abbrev-commit"',
    )
    parser.add_argument(
        "--show-signature",
        action="store_true",
        help="Check the validity of a signed commit object by passing the signature to gpg --verify and show the output",
    )
    parser.add_argument(
        "--date",
        help="Only takes effect for dates shown in human-readable format, such as when using --pretty",
    )
    parser.add_argument(
        "--relative-date",
        action="store_true",
        help="Synonym for --date=relative",
    )

    parser.add_argument("revision_range", nargs="?")
    parser.add_argument("path", nargs=argparse.REMAINDER)


def main(cmd: Annotated[Optional[str], yapx.arg(None, pos=True)]):
    parser = yapx.ArgumentParser(prog="git")

    subparsers = parser.add_subparsers()

    git_commit(subparsers.add_parser("commit"))
    git_log(subparsers.add_parser("log"))
    git_merge(subparsers.add_parser("merge"))

    invoke_tui(parser, command_filter=cmd)
