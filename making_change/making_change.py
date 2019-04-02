#!/usr/bin/python

import sys


def making_change(amount, denominations):
    ways_making_change = [0] * (amount + 1)

    ways_making_change[0] = 1

    for coins in denominations:
        for high_amt in range(coins, amount + 1):
            remainder = high_amt - coins
            ways_making_change[high_amt] += ways_making_change[remainder]
    return ways_making_change[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
