import yapx


def pastel_color(subparser):
    subparser.prog = "pastel color"
    subparser.description = "Show and display some information about the given color(s)"

    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_list(subparser):
    subparser.prog = "pastel list"
    subparser.description = "Show a list of available color names"

    subparser.add_argument(
        "-s",
        "--sort",
        dest="sort_order",
        default="hue",
        choices=["brightness", "luminance", "hue", "chroma", "random"],
        help="Sort order",
    )


def pastel_random(subparser):
    subparser.prog = "pastel random"
    subparser.description = "Generate a list of random colors"

    subparser.add_argument(
        "-s",
        "--strategy",
        dest="random_strategy",
        default="vivid",
        choices=["vivid", "rgb", "gray", "lch_hue"],
        help="Randomization strategy",
    )
    subparser.add_argument(
        "-n",
        "--number",
        dest="color_count",
        type=int,
        default=10,
        help="Number of colors to generate",
    )


def pastel_distinct(subparser):
    subparser.prog = "pastel distinct"
    subparser.description = "Generate a set of visually distinct colors by maximizing the perceived color difference between pairs of colors"

    subparser.add_argument(
        "count",
        type=int,
        default=10,
        help="Number of distinct colors in the set",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )

    subparser.add_argument(
        "-m",
        "--metric",
        dest="distance_metric",
        default="CIE76",
        choices=["CIEDE2000", "CIE76"],
        help="Distance metric to compute mutual color distances",
    )
    subparser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print simulation output to STDERR",
    )


def pastel_sort_by(subparser):
    subparser.prog = "pastel sort-by"
    subparser.description = "Sort a list of colors by the given property."

    subparser.add_argument(
        "sort_order",
        nargs="?",
        choices=["brightness", "luminance", "hue", "chroma", "random"],
        default="hue",
        help="Sort order [default: hue]",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors to sort. Use various formats (hex, rgb, hsl, named color).",
    )
    subparser.add_argument(
        "-r",
        "--reverse",
        action="store_true",
        help="Reverse the sort order",
    )
    subparser.add_argument(
        "-u",
        "--unique",
        action="store_true",
        help="Remove duplicate colors",
    )


def pastel_format(subparser):
    subparser.prog = "pastel format"
    subparser.description = "Convert the given color(s) to a specific format."

    subparser.add_argument(
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
        default="hex",
        help="Output format type.",
    )

    # Define the <color> argument
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors to convert to the specified format.",
    )


def pastel_paint(subparser):
    subparser.prog = "pastel paint"
    subparser.description = "Print colored text using ANSI escape sequences"

    # Add the positional arguments
    subparser.add_argument(
        "color",
        help="The foreground color.",
    )
    subparser.add_argument(
        "text",
        nargs="+",
        help="The text to be printed in color.",
    )

    # Add the optional arguments
    subparser.add_argument(
        "-o",
        "--on",
        metavar="bg-color",
        help="Use the specified background color",
    )
    subparser.add_argument(
        "-b",
        "--bold",
        action="store_true",
        help="Print the text in bold face",
    )
    subparser.add_argument(
        "-i",
        "--italic",
        action="store_true",
        help="Print the text in italic font",
    )
    subparser.add_argument(
        "-u",
        "--underline",
        action="store_true",
        help="Draw a line below the text",
    )
    subparser.add_argument(
        "-n",
        "--no-newline",
        action="store_true",
        help="Do not print a trailing newline character",
    )


def pastel_gradient(subparser):
    subparser.prog = "pastel gradient"
    subparser.description = (
        "Generate a sequence of colors that interpolates between the specified colors."
    )

    subparser.add_argument("color", nargs="+", help="Color stops in the color gradient")
    subparser.add_argument(
        "-n",
        "--number",
        type=int,
        default=10,
        help="Number of colors to generate [default: 10]",
    )
    subparser.add_argument(
        "-s",
        "--colorspace",
        choices=["Lab", "LCh", "RGB", "HSL"],
        default="Lab",
        help="The colorspace in which to interpolate [default: Lab]",
    )


def pastel_mix(subparser):
    subparser.prog = "pastel mix"
    subparser.description = (
        "Create new colors by interpolating between two colors in the given colorspace"
    )

    subparser.add_argument(
        "color",
        help="The base color which will be mixed with the other colors",
    )
    subparser.add_argument(
        "other_colors",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )
    subparser.add_argument(
        "-s",
        "--colorspace",
        choices=["Lab", "LCh", "RGB", "HSL"],
        default="Lab",
        help="The colorspace in which to interpolate",
    )
    subparser.add_argument(
        "-f",
        "--fraction",
        type=float,
        default=0.5,
        help="The number between 0.0 and 1.0 determining how much to mix in from the base color",
    )


def pastel_colorblind(subparser):
    subparser.prog = "pastel colorblind"
    subparser.description = "Convert the given color to how it would look to a person with protanopia, deuteranopia, or tritanopia"

    subparser.add_argument(
        "type",
        choices=["prot", "deuter", "trit"],
        help="The type of colorblindness that should be simulated (protanopia, deuteranopia, tritanopia)",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_set(subparser):
    subparser.prog = "pastel set"
    subparser.description = "Set the given property to a specific value"

    subparser.add_argument(
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
    subparser.add_argument("value", help="The new numerical value of the property")
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_saturate(subparser):
    subparser.prog = "pastel saturate"
    subparser.description = "Increase the saturation of a color by adding a certain amount to the HSL saturation channel."

    subparser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to add (number between 0.0 and 1.0)",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_desaturate(subparser):
    subparser.prog = "pastel desaturate"
    subparser.description = "Decrease the saturation of a color by subtracting a certain amount from the HSL saturation channel."

    subparser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to subtract (number between 0.0 and 1.0)",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_lighten(subparser):
    subparser.prog = "pastel lighten"
    subparser.description = (
        "Lighten a color by adding a certain amount to the HSL lightness channel."
    )

    subparser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to add (number between 0.0 and 1.0)",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_darken(subparser):
    subparser.prog = "pastel darken"
    subparser.description = (
        "Darken a color by subtracting a certain amount from the lightness channel."
    )

    subparser.add_argument(
        "amount",
        type=float,
        help="Amount of saturation to subtract (number between 0.0 and 1.0)",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_rotate(subparser):
    subparser.prog = "pastel rotate"
    subparser.description = "Rotate the HSL hue channel of a color by the specified angle (in degrees). A rotation by 180° returns the complementary color. A rotation by 360° returns to the original color."

    subparser.add_argument(
        "degrees",
        type=float,
        help="angle by which to rotate (in degrees, can be negative)",
    )
    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_complement(subparser):
    subparser.prog = "pastel complement"
    subparser.description = (
        "Compute the complementary color by rotating the HSL hue channel by 180°."
    )

    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_gray(subparser):
    subparser.prog = "pastel gray"
    subparser.description = "Create a gray tone from a given lightness value."

    subparser.add_argument(
        "lightness",
        type=float,
        help="Lightness of the created gray tone (number between 0.0 and 1.0)",
    )


def pastel_to_gray(subparser):
    subparser.prog = "pastel to-gray"
    subparser.description = (
        "Completely desaturate the given color while preserving the luminance."
    )

    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


def pastel_textcolor(subparser):
    subparser.prog = "pastel textcolor"
    subparser.description = "Return a readable foreground text color (either black or white) for a given background color. This can also be used in the opposite way, i.e. to create a background color for a given text color."

    subparser.add_argument(
        "color",
        nargs="+",
        help="Colors can be specified in many different formats, such as #RRGGBB, RRGGBB, #RGB, 'rgb(…, …, …)', 'hsl(…, …, …)', 'gray(…)' or simply by the name of the color.",
    )


parser = yapx.ArgumentParser(
    prog="pastel",
    description="A command-line tool to generate, analyze, convert and manipulate colors",
    add_help=False,
)

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
