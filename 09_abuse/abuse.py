#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-10-01
Purpose: Generating random insults from lists of words
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Heap abuse", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="Number of adjectives",
        metavar="adjectives",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="Number of insults",
        metavar="number",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    args = parser.parse_args()
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    elif args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    else:
        return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    adjectives = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false
    filthsome filthy foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome lubbery old peevish
    rascaly rotten ruinous scurilous scurvy slanderous sodden-witted
    thin-faced toad-spotted unmannered vile wall-eyed
    """.strip().split()

    nouns = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt
    carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    gull harpy jack jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    """.strip().split()

    args = get_args()
    random.seed(args.seed)
    for n in range(args.number):
        adj = random.sample(adjectives, args.adjectives)

        noun = random.choice(nouns)
        print("You {} {}!".format(", ".join(adj), "".join(noun)))


# --------------------------------------------------
if __name__ == "__main__":
    main()
