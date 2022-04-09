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


def make_report(portfolio_filename, prices_filename):
    '''Compute gain and loss'''
    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    total_gain_loss = 0
    print(f"{'Name':>10s} {'Shares':>10} {'Price':>10} {'Change':>10}")
    print(f"{'':->10s} {'':->10s} {'':->10s} {'':->10s}")
    
    for row in portfolio:
        previous_value = row['shares'] * row['price']
        actual_price = prices.get(row['name'], 0.0)
        if actual_price:
            actual_value =  actual_price * row['shares']
            total_gain_loss += (actual_value - previous_value)
            print(f"{row['name']:>10s} {row['shares']:>10d} {actual_price:>10,.2f} {actual_price - row['price']:>10,.2f}")
        else:
            print(f"{row['name']:>10s} {row['shares']:>10d} {'None':>10s} {'':?>10s}")
    
    print(f"\nTotal gain/loss: {total_gain_loss:10,.2f}")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        protfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'
    
    make_report(portfolio_filename, prices_filename)

