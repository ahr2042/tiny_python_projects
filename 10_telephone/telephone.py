#!/usr/bin/env python3
"""
Author : A-Rashed <Rashed-a@web.de>
Date   : 2023-10-02
Purpose: Randomly mutating strings
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()
    if args.mutations >= 0.0 and args.mutations <= 1.0:
        return args
    else:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if os.path.isfile(args.text):
        text = open(args.text).read().rstrip()
    else:
        text = args.text

    random.seed(args.seed)

    num_mutations = round(len(text) * args.mutations)
    alpha = "".join(sorted(string.ascii_letters + string.punctuation))

    print(f'You said: "{text}"')

    # deterministic approach
    indexes = random.sample(range(len(text)), num_mutations)
    for i in indexes:
        text = text[:i] + random.choice(alpha.replace(text[i], "")) + text[i + 1 :]

    print(f'I heard : "{text}"')

    # non-deterministic approach (faster and less mem usage for large text files)
    """ 
    new_text = ''
    for char in text:
        new_text += random.choice(alpha) if random.random() <= args.mutations else char
    print(f'I heard : "{new_text}"')
    """


# --------------------------------------------------
if __name__ == "__main__":
    main()
