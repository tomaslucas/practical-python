# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_price = 0
    with open(filename, 'rt') as f:
        try:
            rows = csv.reader(f)
            header = next(rows)
            for row in rows:
                total_price += int(row[1]) * float(row[2])
        except Exception as e:
            print('Error encontrado en el fichero: ', e)

    return total_price

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    
    cost = portfolio_cost(filename)
    print('Total cost:', cost)