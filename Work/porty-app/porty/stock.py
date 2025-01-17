from . import typedproperty

class Stock():
    name = typedproperty.String('name')
    shares = typedproperty.Integer('shares')
    price = typedproperty.Float('price')

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    def sell(self, shares_sold):
        self.shares -= shares_sold

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"


class NewStock(Stock):
    def yow(self):
        print('Yow!')

