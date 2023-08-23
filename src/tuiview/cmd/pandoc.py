import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(
    prog="pandoc",
    description="Convert files between different document formats.",
    add_help=False,
)

# Add options and arguments
parser.add_argument(
    "-f",
    "--from",
    "--read",
    dest="input_format",
    help="Specify the input format",
)
parser.add_argument(
    "-t",
    "--to",
    "--write",
    dest="output_format",
    help="Specify the output format",
)
parser.add_argument(
    "-o",
    "--output",
    dest="output_file",
    help="Specify the output file",
)
parser.add_argument("--data-dir", dest="data_dir", help="Specify the data directory")
parser.add_argument(
    "-M",
    "--metadata",
    dest="metadata",
    nargs="+",
    help="Specify metadata as key value pairs",
)
parser.add_argument(
    "--metadata-file",
    dest="metadata_file",
    help="Specify the metadata file",
)
parser.add_argument(
    "-d",
    "--defaults",
    dest="defaults",
    help="Specify the defaults file",
)
parser.add_argument(
    "--file-scope",
    dest="file_scope",
    action="store_true",
    help="Enable file-scoped variables",
)
parser.add_argument(
    "-s",
    "--standalone",
    dest="standalone",
    action="store_true",
    help="Generate a standalone document",
)
parser.add_argument("--template", dest="template", help="Specify the template file")
parser.add_argument(
    "-V",
    "--variable",
    dest="variables",
    nargs="+",
    help="Specify variables as key value pairs",
)
parser.add_argument(
    "--wrap",
    dest="wrap",
    choices=["auto", "none", "preserve"],
    help="Specify wrapping behavior",
)
parser.add_argument(
    "--ascii",
    dest="ascii",
    action="store_true",
    help="Use only ASCII characters",
)
parser.add_argument(
    "--toc",
    "--table-of-contents",
    dest="toc",
    action="store_true",
    help="Include table of contents",
)
parser.add_argument(
    "--toc-depth",
    dest="toc_depth",
    type=int,
    help="Specify the depth of the table of contents",
)
parser.add_argument(
    "-N",
    "--number-sections",
    dest="number_sections",
    action="store_true",
    help="Number sections",
)
parser.add_argument(
    "--number-offset",
    dest="number_offset",
    nargs="+",
    help="Specify the number offset",
)
parser.add_argument(
    "--top-level-division",
    dest="top_level_division",
    choices=["section", "chapter", "part"],
    help="Specify the top level division",
)
parser.add_argument(
    "--extract-media",
    dest="extract_media",
    help="Specify the path to extract media files",
)
parser.add_argument(
    "--resource-path",
    dest="resource_path",
    help="Specify the search path for resources",
)
parser.add_argument(
    "-H",
    "--include-in-header",
    dest="include_header",
    help="Include file contents at the beginning",
)
parser.add_argument(
    "-B",
    "--include-before-body",
    dest="include_before_body",
    help="Include file contents before the body",
)
parser.add_argument(
    "-A",
    "--include-after-body",
    dest="include_after_body",
    help="Include file contents after the body",
)
parser.add_argument(
    "--no-highlight",
    dest="no_highlight",
    action="store_true",
    help="Disable syntax highlighting",
)
parser.add_argument(
    "--highlight-style",
    dest="highlight_style",
    help="Specify the highlighting style",
)
parser.add_argument(
    "--syntax-definition",
    dest="syntax_definition",
    help="Specify the syntax definition file",
)
parser.add_argument("--dpi", dest="dpi", type=int, help="Specify the DPI")
parser.add_argument(
    "--eol",
    dest="eol",
    choices=["crlf", "lf", "native"],
    help="Specify the end-of-line type",
)
parser.add_argument(
    "--columns",
    dest="columns",
    type=int,
    help="Specify the number of columns",
)
parser.add_argument(
    "-p",
    "--preserve-tabs",
    dest="preserve_tabs",
    action="store_true",
    help="Preserve tabs",
)
parser.add_argument(
    "--tab-stop",
    dest="tab_stop",
    type=int,
    help="Specify the tab stop",
)
parser.add_argument("--pdf-engine", dest="pdf_engine", help="Specify the PDF engine")
parser.add_argument(
    "--pdf-engine-opt",
    dest="pdf_engine_opt",
    help="Specify the PDF engine options",
)
parser.add_argument(
    "--reference-doc",
    dest="reference_doc",
    help="Specify the reference document",
)
parser.add_argument(
    "--self-contained",
    dest="self_contained",
    action="store_true",
    help="Produce a self-contained HTML document",
)
parser.add_argument(
    "--request-header",
    dest="request_header",
    nargs="+",
    help="Specify request headers",
)
parser.add_argument(
    "--abbreviations",
    dest="abbreviations",
    help="Specify the abbreviations file",
)
parser.add_argument(
    "--indented-code-classes",
    dest="indented_code_classes",
    help="Specify indented code classes",
)
parser.add_argument(
    "--default-image-extension",
    dest="default_image_extension",
    help="Specify the default image extension",
)
parser.add_argument("-F", "--filter", dest="filter", help="Specify the filter program")
parser.add_argument(
    "-L",
    "--lua-filter",
    dest="lua_filter",
    help="Specify the Lua filter script",
)
parser.add_argument(
    "--shift-heading-level-by",
    dest="shift_heading_level",
    type=int,
    help="Specify the shift of heading levels",
)
parser.add_argument(
    "--base-header-level",
    dest="base_header_level",
    type=int,
    help="Specify the base header level",
)
parser.add_argument(
    "--strip-empty-paragraphs",
    dest="strip_empty_paragraphs",
    action="store_true",
    help="Strip empty paragraphs",
)
parser.add_argument(
    "--track-changes",
    dest="track_changes",
    choices=["accept", "reject", "all"],
    help="Specify how to track changes",
)
parser.add_argument(
    "--strip-comments",
    dest="strip_comments",
    action="store_true",
    help="Strip comments",
)
parser.add_argument(
    "--reference-links",
    dest="reference_links",
    action="store_true",
    help="Use reference links",
)
parser.add_argument(
    "--reference-location",
    dest="reference_location",
    choices=["block", "section", "document"],
    help="Specify the reference location",
)
parser.add_argument(
    "--atx-headers",
    dest="atx_headers",
    action="store_true",
    help="Use ATX-style headers",
)
parser.add_argument(
    "--listings",
    dest="listings",
    action="store_true",
    help="Use listings for code blocks",
)
parser.add_argument(
    "-i",
    "--incremental",
    dest="incremental",
    action="store_true",
    help="Generate incremental HTML",
)
parser.add_argument(
    "--slide-level",
    dest="slide_level",
    type=int,
    help="Specify the slide level",
)
parser.add_argument(
    "--section-divs",
    dest="section_divs",
    action="store_true",
    help="Use section divs",
)
parser.add_argument(
    "--html-q-tags",
    dest="html_q_tags",
    action="store_true",
    help="Use q tags for quotes",
)
parser.add_argument(
    "--email-obfuscation",
    dest="email_obfuscation",
    choices=["none", "javascript", "references"],
    help="Specify email obfuscation technique",
)
parser.add_argument("--id-prefix", dest="id_prefix", help="Specify the ID prefix")
parser.add_argument(
    "-T",
    "--title-prefix",
    dest="title_prefix",
    help="Specify the title prefix",
)
parser.add_argument("-c", "--css", dest="css", help="Specify the CSS file")
parser.add_argument(
    "--epub-subdirectory",
    dest="epub_subdirectory",
    help="Specify the EPUB subdirectory",
)
parser.add_argument(
    "--epub-cover-image",
    dest="epub_cover_image",
    help="Specify the EPUB cover image",
)
parser.add_argument(
    "--epub-metadata",
    dest="epub_metadata",
    help="Specify the EPUB metadata file",
)
parser.add_argument(
    "--epub-embed-font",
    dest="epub_embed_font",
    help="Specify the EPUB embed font",
)
parser.add_argument(
    "--epub-chapter-level",
    dest="epub_chapter_level",
    type=int,
    help="Specify the EPUB chapter level",
)
parser.add_argument(
    "--ipynb-output",
    dest="ipynb_output",
    choices=["all", "none", "best"],
    help="Specify how to handle IPYNB outputs",
)
parser.add_argument(
    "--bibliography",
    dest="bibliography",
    help="Specify the bibliography file",
)
parser.add_argument("--csl", dest="csl", help="Specify the CSL file")
parser.add_argument(
    "--citation-abbreviations",
    dest="citation_abbreviations",
    help="Specify the citation abbreviations file",
)
parser.add_argument(
    "--natbib",
    dest="natbib",
    action="store_true",
    help="Enable natbib",
)
parser.add_argument(
    "--biblatex",
    dest="biblatex",
    action="store_true",
    help="Enable biblatex",
)
parser.add_argument(
    "--mathml",
    dest="mathml",
    action="store_true",
    help="Enable MathML",
)
parser.add_argument(
    "--webtex",
    dest="webtex",
    nargs="?",
    const="",
    help="Enable webTeX with optional URL",
)
parser.add_argument(
    "--mathjax",
    dest="mathjax",
    nargs="?",
    const="",
    help="Enable MathJax with optional URL",
)
parser.add_argument(
    "--katex",
    dest="katex",
    nargs="?",
    const="",
    help="Enable KaTeX with optional URL",
)
parser.add_argument(
    "--gladtex",
    dest="gladtex",
    action="store_true",
    help="Enable gladTeX",
)
parser.add_argument(
    "--trace",
    dest="trace",
    action="store_true",
    help="Enable trace mode",
)
parser.add_argument(
    "--dump-args",
    dest="dump_args",
    action="store_true",
    help="Dump parsed command-line arguments",
)
parser.add_argument(
    "--ignore-args",
    dest="ignore_args",
    action="store_true",
    help="Ignore unknown arguments",
)
parser.add_argument(
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Enable verbose mode",
)
parser.add_argument(
    "--quiet",
    dest="quiet",
    action="store_true",
    help="Suppress all output except errors",
)
parser.add_argument(
    "--fail-if-warnings",
    dest="fail_if_warnings",
    action="store_true",
    help="Fail if there are warnings",
)
parser.add_argument("--log", dest="log", help="Specify the log file")
parser.add_argument(
    "--bash-completion",
    dest="bash_completion",
    action="store_true",
    help="Enable Bash completion",
)
parser.add_argument(
    "--list-input-formats",
    dest="list_input_formats",
    action="store_true",
    help="List available input formats",
)
parser.add_argument(
    "--list-output-formats",
    dest="list_output_formats",
    action="store_true",
    help="List available output formats",
)
parser.add_argument(
    "--list-extensions",
    dest="list_extensions",
    nargs="?",
    const="FORMAT",
    help="List available extensions for specified format",
)
parser.add_argument(
    "--list-highlight-languages",
    dest="list_highlight_languages",
    action="store_true",
    help="List available highlight languages",
)
parser.add_argument(
    "--list-highlight-styles",
    dest="list_highlight_styles",
    action="store_true",
    help="List available highlight styles",
)
parser.add_argument(
    "-D",
    "--print-default-template",
    dest="print_default_template",
    help="Print default template for specified format",
)
parser.add_argument(
    "--print-default-data-file",
    dest="print_default_data_file",
    help="Print default data file",
)
parser.add_argument(
    "--print-highlight-style",
    dest="print_highlight_style",
    help="Print default highlight style file",
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="%(prog)s 1.0",
    help="Print version information",
)
