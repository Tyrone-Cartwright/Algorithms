#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    output = []
    if n == 0:
        return [[]]
    elif n == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        for choice in rock_paper_scissors(n-1):
            output = output + [choice + ['rock'], choice +
                               ['paper'], choice + ['scissors'], ]
    return output


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
