#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-09-27
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", nargs="+", metavar="letter", type=str, help="Letter(s)"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="File",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    ans = dict()

    for letter in args.letter:
        for line in args.file:
            if letter.lower() == line[0].lower():
                ans[letter.lower()] = line
                break

    for letter in args.letter:
        if letter.lower() in ans:
            print(ans[letter.lower()], end="")
        else:
            print('I do not know "{}".'.format(letter))


# --------------------------------------------------
if __name__ == "__main__":
    main()
