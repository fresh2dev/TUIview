import argparse

# Create the parser
parser = argparse.ArgumentParser(
    prog="cloc",
    description="Count, or compute differences of, physical lines of source code",
    add_help=False,
)

# Add the usage option
parser.add_argument("files", nargs="*", help="file(s)/dir(s)/git hash(es)")

# Add the input options
input_options = parser.add_argument_group("Input Options")
input_options.add_argument(
    "--extract-with",
    help="Use <cmd> to extract binary archive files",
)
input_options.add_argument(
    "--list-file",
    help="Take the list of file and/or directory names to process from <file>",
)
input_options.add_argument(
    "--diff-list-file",
    help="Take the pairs of file names to be diff'ed from <file>",
)
input_options.add_argument(
    "--vcs",
    help="Invoke a system call to <VCS> to obtain a list of files to work on",
)
input_options.add_argument(
    "--unicode",
    action="store_true",
    help="Check binary files to see if they contain Unicode expanded ASCII text",
)

# Add the processing options
processing_options = parser.add_argument_group("Processing Options")
processing_options.add_argument(
    "--autoconf",
    action="store_true",
    help="Count .in files (as processed by GNU autoconf) of recognized languages",
)
processing_options.add_argument(
    "--by-file",
    action="store_true",
    help="Report results for every source file encountered",
)
processing_options.add_argument(
    "--by-file-by-lang",
    action="store_true",
    help="Report results for every source file encountered in addition to reporting by language",
)
processing_options.add_argument(
    "--config",
    help="Read command line switches from <file> instead of the default location",
)
processing_options.add_argument(
    "--count-and-diff",
    nargs=2,
    metavar=("set1", "set2"),
    help="First perform direct code counts of source file(s) of <set1> and <set2> separately, then perform a diff of these",
)
processing_options.add_argument(
    "--diff",
    nargs=2,
    metavar=("set1", "set2"),
    help="Compute differences in code and comments between source file(s) of <set1> and <set2>",
)
processing_options.add_argument(
    "--diff-timeout",
    type=int,
    metavar="N",
    help="Ignore files which take more than <N> seconds to process",
)
processing_options.add_argument(
    "--docstring-as-code",
    action="store_true",
    help="cloc considers docstrings to be comments",
)
processing_options.add_argument(
    "--follow-links",
    action="store_true",
    help="[Unix only] Follow symbolic links to directories",
)
processing_options.add_argument(
    "--force-lang",
    nargs="+",
    action="append",
    help="Process all files that have a <ext> extension with the counter for language <lang>",
)
processing_options.add_argument(
    "--force-lang-def",
    help="Load language processing filters from <file>",
)
processing_options.add_argument(
    "--git",
    action="store_true",
    help="Forces the inputs to be interpreted as git targets",
)
processing_options.add_argument(
    "--git-diff-rel",
    action="store_true",
    help="Same as --git --diff",
)
processing_options.add_argument(
    "--git-diff-all",
    action="store_true",
    help="Git diff strategy #2: compare all files in the repository between the two commits",
)
processing_options.add_argument(
    "--ignore-whitespace",
    action="store_true",
    help="Ignore horizontal white space when comparing files with --diff",
)
processing_options.add_argument(
    "--ignore-case",
    action="store_true",
    help="Ignore changes in case within file contents when comparing files with --diff",
)
processing_options.add_argument(
    "--ignore-case-ext",
    action="store_true",
    help="Ignore case of file name extensions",
)
processing_options.add_argument(
    "--lang-no-ext",
    help="Count files without extensions using the <lang>",
)
