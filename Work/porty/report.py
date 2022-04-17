#!/usr/bin/env python
# report.py
#
# Exercise 2.4
# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)


import csv
import sys

from . import fileparse
from . import portfolio
from . import tableformat

def read_portfolio(filename:str, **opts) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as file:
        return portfolio.Portfolio.from_csv(file, **opts)

def read_prices(filename:str, types=[str,float], has_headers=False) -> dict:
    '''
    It reads a set of prices where the keys are the stock names and the value 
    are the stock prices.
    '''
    with open(filename, 'rt') as file:
        return dict(fileparse.parse_csv(file=file, types=types, has_headers=has_headers))
    

def make_report(portfolio, prices):
    '''Create a new dictionary with the new value and the difference with previous price.'''
    report = []
    headers = ('Name', 'Shares', 'Price', 'Change')
    report.append(headers)
    for row in portfolio:
        actual_price = prices.get(row.name, 0.0)
        holding = (row.name, row.shares, actual_price, actual_price - row.price)
        report.append(holding) 
    return report


def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata[1:]:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
    

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


if __name__ == '__main__':
    if len(sys.argv) == 4:
        protfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
        fmt = sys.argv[3]
        portfolio_report(protfolio_filename, prices_filename, fmt)
    else:
        files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
        prices_filename = 'Data/prices.csv'
        for name in files:
            print(f'{name:-^43s}')
            portfolio_report(name, prices_filename)
            print()




