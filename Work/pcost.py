# pcost.py
#
# Exercise 1.27
import csv
import sys

from report import read_portfolio

def portfolio_cost(filename):
    portfolio = read_portfolio(filename)
    return sum([record['shares'] * record['price'] for record in portfolio])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
        
    cost = portfolio_cost(filename)
    print('Total cost:', cost)