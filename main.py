#! /usr/bin/env python3
# This program displays change in bills
import argparse

denominations = {'one-hundred dollar': 100.00, 'fifty dollar': 50.00, 'twenty dollar': 20.00, 'ten dollar': 10.00,
                 'five dollar': 5.00, 'dollar': 1.00, 'quarter': 0.25, 'dime': 0.10, 'nickle': 0.05, 'penny': 0.01}

change = {'penny': 0, 'nickle': 0, 'dime': 0, 'quarter': 0, 'dollar': 0, 'five dollar': 0, 'ten dollar': 0,
          'twenty dollar': 0, 'fifty dollar': 0, 'one-hundred dollar': 0, 'Total change': 0}


def main(n):
    calculate(n)
    print_change()


def calculate(n):
    for key in denominations:
        while True:
            if denominations[key] > n:
                break
            n = round(n - denominations[key], 2)
            change['Total change'] = round(change['Total change'] + denominations[key], 2)
            change[key] += 1


def print_change():
    # prints change in 'penny: 1' format
    for note in change:
        if change[note] != 0:
            print(f'{note}: ' + str(change[note]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple program that displays change in USD currency.')
    parser.add_argument('change', type=float, help='Value to be converted, cannot be less than zero.')

    args = parser.parse_args()

    if args.change < 0:
        print('Error! Value must be greater than zero!')

    main(args.change)
