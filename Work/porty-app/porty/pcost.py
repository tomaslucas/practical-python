#!/usr/bin/env python
# pcost.py
#
# Exercise 1.27
import csv
import sys

from . import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
    #return sum([record.cost for record in portfolio])
    #return sum([record.shares * record.price for record in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
