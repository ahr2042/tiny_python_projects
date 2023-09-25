#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-09-24
Purpose: Working with files and STDOUT
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-case input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input string or file")

    parser.add_argument(
        "-o", "--outfile", help="Output filename", metavar="str", default=""
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    message = (
        open(args.text).read().rstrip() if os.path.isfile(args.text) else args.text
    )
    if args.outfile:
        out_fh = open(args.outfile, "wt")
        out_fh.write(message.upper() + "\n")
        out_fh.close()
    else:
        print(message.upper())


# --------------------------------------------------
if __name__ == "__main__":
    main()
