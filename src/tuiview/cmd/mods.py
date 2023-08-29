import argparse

parser = argparse.ArgumentParser(
    prog="mods",
    description="GPT on the command line. Built for pipelines.",
    add_help=False,
)

parser.add_argument("TERM", nargs="?", help="Term")

parser.add_argument(
    "-m",
    "--model",
    help="Default model (gpt-3.5-turbo, gpt-4, ggml-gpt4all-j...).",
)
parser.add_argument("-a", "--api", help="OpenAI compatible REST API (openai, localai).")
parser.add_argument(
    "-f",
    "--format",
    action="store_true",
    help="Format response as markdown.",
)
parser.add_argument(
    "-P",
    "--prompt",
    action="store_true",
    help="Include the prompt from the arguments and stdin, truncate stdin to specified number of lines.",
)
parser.add_argument(
    "-p",
    "--prompt-args",
    action="store_true",
    help="Include the prompt from the arguments in the response.",
)
parser.add_argument(
    "-q",
    "--quiet",
    action="store_true",
    help="Quiet mode (hide the spinner while loading).",
)
parser.add_argument(
    "-s",
    "--settings",
    action="store_true",
    help="Open settings in your $EDITOR.",
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="1.0",
    help="Show version and exit.",
)
parser.add_argument("--max-retries", help="Maximum number of times to retry API calls.")
parser.add_argument(
    "--no-limit",
    action="store_true",
    help="Turn off the client-side limit on the size of the input into the model.",
)
parser.add_argument("--max-tokens", help="Maximum number of tokens in response.")
parser.add_argument(
    "--temp",
    help="Temperature (randomness) of results, from 0.0 to 2.0.",
)
parser.add_argument(
    "--topp",
    help="TopP, an alternative to temperature that narrows response, from 0.0 to 1.0.",
)
parser.add_argument(
    "--fanciness",
    help='Number of cycling characters in the "generating" animation.',
)
parser.add_argument("--status-text", help="Text to show while generating.")
