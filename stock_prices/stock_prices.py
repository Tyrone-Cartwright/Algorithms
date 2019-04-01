#!/usr/bin/python

import argparse


def find_max_profit(prices):
    buy = prices[0]
    sell = prices[1]
    for index, price in enumerate(prices):
        if buy == prices[len(prices)-2]:
            return prices[len(prices)-1] - buy

        if index <= prices[len(prices)-1]:
            if buy > price:
                buy = price
            if (index+1) <= (len(prices)-1) and sell < prices[index+1]:
                sell = prices[index+1]

    return (sell - buy)


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
