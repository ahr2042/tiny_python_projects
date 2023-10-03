#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-10-03
Purpose: Randomly capitalizing text
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    if os.path.isfile(args.text):
        text = open(args.text).read().rstrip()
    else:
        text = args.text
    for i in text:
        print(choose(i), end="")
    print("")


# ----------------------------
def choose(char):
    if random.choice([True, False]):
        return char.lower()
    else:
        return char.upper()


# ---------------------
def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)


# --------------------------------------------------
if __name__ == "__main__":
    main()
