#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-09-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("food", metavar="str", nargs="+", help="Item to bring")

    parser.add_argument("-s", "--sorted", action="store_true", help="Sort the items")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    food_arg = args.food
    length = len(food_arg)

    if args.sorted:
        food_arg.sort()

    if length > 2:
        cc = "and " + food_arg.pop()
        food_arg.append(cc)

    if length == 1:
        print("You are bringing {}.".format(food_arg[0]))
    elif length == 2:
        print("You are bringing {} and {}.".format(food_arg[0], food_arg[1]))
    else:
        print("You are bringing {}.".format(", ".join(food_arg)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
