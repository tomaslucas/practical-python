# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total_price = 0
    with open(filename, 'rt') as f:
        try:
            header = next(f)
            for line in f:
                l = line.strip().split(',')
                total_price += int(l[1]) * float(l[2])
        except Exception as e:
            print('Error encontrado en el fichero: ', e)

    return total_price

if __name__ == '__main__':
    cost = portfolio_cost('Data/portfolio.csv')
    print('Total cost:', cost)