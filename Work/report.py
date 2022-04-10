# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename:str) -> list:
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        types = [str, int, float]
        indices = [headers.index(colname) for colname in select]
        return [{colname: func(row[index]) for colname, index, func in zip(select, indices, types)} for row in rows]


def read_prices(filename:str) -> dict:
    '''
    It reads a set of prices where the keys are the stock names and the value 
    are the stock prices.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        return {row[0]: float(row[1]) for row in rows if len(row) > 0}
    

def make_report(portfolio, prices):
    '''Create a new dictionary with the new value and the difference with previous price.'''
    report = []
    headers = ('Name', 'Shares', 'Price', 'Change')
    report.append(headers)
    for row in portfolio:
        actual_price = prices.get(row['name'], 0.0)
        holding = (row['name'], row['shares'], actual_price, actual_price - row['price'])
        report.append(holding) 
    return report


def print_report(report):
    '''Paint the report.'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report[1:]:
        print(f"{name:>10s} {shares:>10d} {'$' + str(round(price,2)):>10s} {change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        protfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
        portfolio_report(protfolio_filename, prices_filename)
    else:
        files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
        prices_filename = 'Data/prices.csv'
        for name in files:
            print(f'{name:-^43s}')
            portfolio_report(name, prices_filename)
            print()




