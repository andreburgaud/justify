"""
Justify text
"""

from typing import List

import argparse
import itertools
import random
import re
import sys
import textwrap

VERSION = "0.7.0"

LICENSE = """
Copyright 2019 Andre Burgaud

Permission is hereby granted, free  of charge, to any person obtaining a copy of
this software and associated documentation  files (the "Software"),  to  deal in
the Software without restriction,  including without  limitation the  rights  to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit  persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice  and this permission notice shall be included in  all
copies or substantial portions of the Software.

THE SOFTWARE  IS PROVIDED "AS  IS",  WITHOUT  WARRANTY  OF ANY  KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE  AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS  OR
COPYRIGHT HOLDERS BE LIABLE FOR  ANY CLAIM, DAMAGES OR OTHER LIABILITY,  WHETHER
IN AN  ACTION  OF  CONTRACT, TORT  OR  OTHERWISE, ARISING  FROM,  OUT  OF OR  IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


def get_separators(
    space_count: int, sep_count: int, padding_count: int, shuffle: bool
) -> List[str]:
    """Create a list of separators (whitespaces)

    Arguments:
    space_count  : minimum number of spaces to add between workds (before padding)
    sep_count    : number of separators (intervals in a line)
    padding_count: number of extra spaces to add and spread in the line. For example
                   for 4 intervals of 2 spaces, it may be necessary to add 2 extra
                   spaces for the line to align to the expectaded number of columns.
    shuffle      : When set to true, the spaces will be randomly spread n the list
                   to ensure that padding will not only be showing on the first few
                   separators.
    """
    seps = [
        a + b
        for a, b in itertools.zip_longest(
            [" " * (space_count + 1)] * sep_count, [" "] * padding_count, fillvalue=""
        )
    ]
    if shuffle:
        random.shuffle(seps)
    return seps


def interleave(words: List[str], separators: List[str]) -> str:
    """Interleave spaces between words give a list of words and a list of separators.

    words     : list of words for a given line
    separators: list of separators to interleave with list of words
    """

    return "".join(
        itertools.chain(*itertools.zip_longest(words, separators, fillvalue=""))
    )


def normalize_ws(text: str) -> str:
    """Normalize white spaces. Eliminate successive whitespace (\n and " ")"""

    words = text.split()
    return " ".join(words)


def justify(text: str, shuffle: bool = True, columns: int = 80) -> str:
    """Justify the text passed as argument, and align to the expected number of
    columns. Shuffle indicate to spread extra padding randomly in the intervals,
    rather than having all of them added to the first separators.
    """

    justified_sections = []

    for section in re.split(r"\n\n+", text):
        if section == "":
            # Preserve empty line
            justified_sections.append(section)
            continue

        section = normalize_ws(section)

        lines = textwrap.wrap(section, columns)

        if len(lines) == 1:
            # No justification if only one line (same as last line of section)
            justified_sections.append(section)
            continue

        new_lines = []

        for line in lines[:-1]:  # Don't justify the last line
            len_line = len(line)
            if len_line == columns:
                # Line already expected length
                # Prevents ZeroDivisionError in divmod
                new_lines.append(line)
                continue
            sep_count = line.count(" ")
            words = line.split()
            missing_spaces = columns - len_line
            space_count, padding_count = divmod(missing_spaces, sep_count)
            separators = get_separators(space_count, sep_count, padding_count, shuffle)
            new_lines.append(interleave(words, separators))

        new_lines.append(lines[-1])  # Add the non justified last line
        justified_sections.append("\n".join(new_lines))

    return "\n\n".join(justified_sections)


def read_stdin() -> str:
    """Read and return content from standard input"""

    data = []
    try:
        for line in sys.stdin:
            data.append(line)
        return "".join(data)
    except KeyboardInterrupt:
        raise SystemExit("")


def read_file(filename: str) -> str:
    """Read a file and return the text"""

    with open(filename, "r") as file:
        data = file.read()
    return data


def print_license() -> None:
    """Print the license"""

    print(LICENSE)
    sys.exit()


def init_argparse() -> argparse.ArgumentParser:
    """Initialize the argument parser"""

    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTIONS] [FILES]...", description="Fully justify text",
    )
    parser.add_argument(
        "-c",
        "--columns",
        help="Number of columns (default: 80)",
        action="store",
        default=80,
        dest="columns",
        type=int,
    )
    parser.add_argument(
        "-l", "--license", help="Display the license", action="store_true",
    )
    parser.add_argument(
        "-s",
        "--shuffle",
        help="Spread whitespace separators randomly on each line",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} {VERSION}"
    )
    parser.add_argument("files", nargs="*")
    return parser


def main():
    """Entrypoint: parse the arguments and trigger the justify processing of the arguments
    or standard in.
    """

    parser = init_argparse()
    args = parser.parse_args()
    shuffle = args.shuffle
    columns = args.columns
    if args.license:
        print_license()
    if not args.files:
        text = read_stdin()
        print(justify(text, shuffle, columns))
    else:
        for file in args.files:
            if file == "-":
                text = read_stdin()
            else:
                try:
                    text = read_file(file)
                except FileNotFoundError:
                    print(f"File {file} not found", file=sys.stderr)
                    continue
            print(justify(text, shuffle, columns))


if __name__ == "__main__":
    main()
