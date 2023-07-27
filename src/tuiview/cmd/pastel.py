from typing import Optional

import yapx
from argparse_tui import invoke_tui
from yapx.types import Annotated


def pastel_color(parser):
    parser.prog = "pastel color"
    parser.description = "Show and display some information about the given color(s)"

    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_list(parser):
    parser.prog = "pastel list"
    parser.description = "Show a list of available color names"

    parser.add_argument(
        "-s",
        "--sort",
        dest="sort_order",
        default="hue",
        choices=["brightness", "luminance", "hue", "chroma", "random"],
        help="Sort order",
    )


def pastel_random(parser):
    parser.prog = "pastel random"
    parser.description = "Generate a list of random colors"

    parser.add_argument(
        "-s",
        "--strategy",
        dest="random_strategy",
        default="vivid",
        choices=["vivid", "rgb", "gray", "lch_hue"],
        help="Randomization strategy",
    )
    parser.add_argument(
        "-n",
        "--number",
        dest="color_count",
        type=int,
        default=10,
        help="Number of colors to generate",
    )


def pastel_distinct(parser):
    parser.prog = "pastel distinct"
    parser.description = "Generate a set of visually distinct colors by maximizing the perceived color difference between pairs of colors"

    parser.add_argument(
        "count",
        type=int,
        default=10,
        help="Number of distinct colors in the set",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )

    parser.add_argument(
        "-m",
        "--metric",
        dest="distance_metric",
        default="CIE76",
        choices=["CIEDE2000", "CIE76"],
        help="Distance metric to compute mutual color distances",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print simulation output to STDERR",
    )


def pastel_sort_by(parser):
    parser.prog = "pastel sort-by"
    parser.description = "Sort a list of colors by the given property."

    parser.add_argument(
        "sort_order",
        nargs="?",
        choices=["brightness", "luminance", "hue", "chroma", "random"],
        default="hue",
        help="Sort order [default: hue]",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors to sort. Use various formats (hex, rgb, hsl, named color).",
    )
    parser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Reverse the sort order",
    )
    parser.add_argument(
        "-u",
        "--unique",
        action="store_true",
        help="Remove duplicate colors",
    )


def pastel_format(parser):
    parser.prog = "pastel format"
    parser.description = "Convert the given color(s) to a specific format."

    parser.add_argument(
        "type",
        choices=[
            "rgb",
            "rgb-float",
            "hex",
            "hsl",
            "hsl-hue",
            "hsl-saturation",
            "hsl-lightness",
            "lch",
            "lch-lightness",
            "lch-chroma",
            "lch-hue",
            "lab",
            "lab-a",
            "lab-b",
            "luminance",
            "brightness",
            "ansi-8bit",
            "ansi-24bit",
            "ansi-8bit-escapecode",
            "ansi-24bit-escapecode",
            "cmyk",
            "name",
        ],
        nargs="?",
        default="hex",
        help="Output format type.",
    )

    # Define the <color> argument
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors to convert to the specified format.",
    )

    # Define the optional arguments
    parser.add_argument(
        "-n",
        metavar="N",
        type=int,
        help="Number of colors to generate.",
    )


def pastel_paint(parser):
    parser.prog = "pastel paint"
    parser.description = "Print colored text using ANSI escape sequences"

    # Add the positional arguments
    parser.add_argument(
        "color",
        help="The foreground color.",
    )
    parser.add_argument(
        "text",
        nargs="+",
        help="The text to be printed in color.",
    )

    # Add the optional arguments
    parser.add_argument(
        "-o",
        "--on",
        metavar="bg-color",
        help="Use the specified background color",
    )
    parser.add_argument(
        "-b",
        "--bold",
        action="store_true",
        help="Print the text in bold face",
    )
    parser.add_argument(
        "-i",
        "--italic",
        action="store_true",
        help="Print the text in italic font",
    )
    parser.add_argument(
        "-u",
        "--underline",
        action="store_true",
        help="Draw a line below the text",
    )
    parser.add_argument(
        "-n",
        "--no-newline",
        action="store_true",
        help="Do not print a trailing newline character",
    )


def pastel_gradient(parser):
    parser.prog = "pastel gradient"
    parser.description = (
        "Generate a sequence of colors that interpolates between the specified colors."
    )

    parser.add_argument("color", nargs="+", help="Color stops in the color gradient")
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=10,
        help="Number of colors to generate [default: 10]",
    )
    parser.add_argument(
        "-s",
        "--colorspace",
        choices=["Lab", "LCh", "RGB", "HSL"],
        default="Lab",
        help="The colorspace in which to interpolate [default: Lab]",
    )


def pastel_mix(parser):
    parser.prog = "pastel mix"
    parser.description = (
        "Create new colors by interpolating between two colors in the given colorspace"
    )

    parser.add_argument(
        "color",
        help="The base color which will be mixed with the other colors",
    )
    parser.add_argument(
        "other_colors",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )
    parser.add_argument(
        "-s",
        "--colorspace",
        choices=["Lab", "LCh", "RGB", "HSL"],
        default="Lab",
        help="The colorspace in which to interpolate",
    )
    parser.add_argument(
        "-f",
        "--fraction",
        type=float,
        default=0.5,
        help="The number between 0.0 and 1.0 determining how much to mix in from the base color",
    )


def pastel_colorblind(parser):
    parser.prog = "pastel colorblind"
    parser.description = "Convert the given color to how it would look to a person with protanopia, deuteranopia, or tritanopia"

    parser.add_argument(
        "type",
        choices=["prot", "deuter", "trit"],
        help="The type of colorblindness that should be simulated (protanopia, deuteranopia, tritanopia)",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_set(parser):
    parser.prog = "pastel set"
    parser.description = "Set the given property to a specific value"

    parser.add_argument(
        "property",
        choices=[
            "lightness",
            "hue",
            "chroma",
            "lab-a",
            "lab-b",
            "red",
            "green",
            "blue",
            "hsl-hue",
            "hsl-saturation",
            "hsl-lightness",
        ],
        help="The property that should be changed",
    )
    parser.add_argument("value", help="The new numerical value of the property")
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_saturate(parser):
    parser.prog = "pastel saturate"
    parser.description = "Increase the saturation of a color by adding a certain amount to the HSL saturation channel."

    parser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to add (number between 0.0 and 1.0)",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_desaturate(parser):
    parser.prog = "pastel desaturate"
    parser.description = "Decrease the saturation of a color by subtracting a certain amount from the HSL saturation channel."

    parser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to add (number between 0.0 and 1.0)",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_lighten(parser):
    parser.prog = "pastel lighten"
    parser.description = (
        "Lighten a color by adding a certain amount to the HSL lightness channel."
    )

    parser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to add (number between 0.0 and 1.0)",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_darken(parser):
    parser.prog = "pastel darken"
    parser.description = (
        "Darken a color by subtracting a certain amount from the lightness channel."
    )

    parser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to add (number between 0.0 and 1.0)",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_rotate(parser):
    parser.prog = "pastel rotate"
    parser.description = "Rotate the HSL hue channel of a color by the specified angle (in degrees). A rotation by 180° returns the complementary color. A rotation by 360° returns to the original color."

    parser.add_argument(
        "degrees",
        type=float,
        help="angle by which to rotate (in degrees, can be negative)",
    )
    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_complement(parser):
    parser.prog = "pastel complement"
    parser.description = (
        "Compute the complementary color by rotating the HSL hue channel by 180°."
    )

    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_gray(parser):
    parser.prog = "pastel gray"
    parser.description = "Create a gray tone from a given lightness value."

    parser.add_argument(
        "lightness",
        type=float,
        help="Lightness of the created gray tone (number between 0.0 and 1.0)",
    )


def pastel_to_gray(parser):
    parser.prog = "pastel to-gray"
    parser.description = (
        "Completely desaturate the given color while preserving the luminance."
    )

    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_textcolor(parser):
    parser.prog = "pastel textcolor"
    parser.description = "Return a readable foreground text color (either black or white) for a given background color. This can also be used in the opposite way, i.e. to create a background color for a given text color."

    parser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def main(cmd: Annotated[Optional[str], yapx.arg(None, pos=True)]):
    parser = yapx.ArgumentParser(prog="pastel")

    subparsers = parser.add_subparsers()

    pastel_color(subparsers.add_parser("color"))
    pastel_list(subparsers.add_parser("list"))
    pastel_random(subparsers.add_parser("random"))
    pastel_distinct(subparsers.add_parser("distinct"))
    pastel_sort_by(subparsers.add_parser("sort-by"))
    pastel_format(subparsers.add_parser("format"))
    pastel_paint(subparsers.add_parser("paint"))
    pastel_gradient(subparsers.add_parser("gradient"))
    pastel_mix(subparsers.add_parser("mix"))
    pastel_colorblind(subparsers.add_parser("colorblind"))
    pastel_set(subparsers.add_parser("set"))
    pastel_saturate(subparsers.add_parser("saturate"))
    pastel_desaturate(subparsers.add_parser("desaturate"))
    pastel_lighten(subparsers.add_parser("lighten"))
    pastel_darken(subparsers.add_parser("darken"))
    pastel_rotate(subparsers.add_parser("rotate"))
    pastel_complement(subparsers.add_parser("complement"))
    pastel_gray(subparsers.add_parser("gray"))
    pastel_to_gray(subparsers.add_parser("to-gray"))
    pastel_textcolor(subparsers.add_parser("textcolor"))

    invoke_tui(parser, command_filter=cmd)
