#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-09-25
Purpose: Words count
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="File",
        nargs="*",
        default=[sys.stdin],
        type=argparse.FileType("rt"),
        help="Input file(s)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines = 0
    total_words = 0
    total_bytes = 0

    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            # get number of lines
            num_lines += 1
            total_lines += 1

            # get number of words
            num_words += len(line.split())
            total_words += len(line.split())

            # get number of bytes
            num_bytes += len(line)
            total_bytes += len(line)

        print("{:8}{:8}{:8} {}".format(num_lines, num_words, num_bytes, fh.name))
    if len(args.file) > 1:
        print("{:8}{:8}{:8} total".format(total_lines, total_words, total_bytes))


# --------------------------------------------------
if __name__ == "__main__":
    main()
