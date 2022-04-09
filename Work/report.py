# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    '''It opens a given portfolio file and reads it into a list of tuples.'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {headers[0]:row[0], headers[1]: int(row[1]), headers[2]: float(row[2])}
            portfolio.append(holding)
            
    return portfolio

def read_prices(filename):
    '''
    It reads a set of prices where the keys are the stock names and the value 
    are rhe stock prices.
    '''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                prices[row[0]] = float(row[1])
    return prices


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

def paint_report(report):
    '''Paint the report.'''
    name, shares, price, change = report[0]
    print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
    print(f"{'':->10s} {'':->10s} {'':->10s} {'':->10s}")
    for name, shares, price, change in report[1:]:
        print(f"{name:>10s} {shares:>10d} {'$' + str(round(price,2)):>10s} {change:>10.2f}")



if __name__ == '__main__':
    if len(sys.argv) == 3:
        protfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'
    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    paint_report(report)


