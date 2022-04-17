# test_sotck_pytest.py
import stock

import pytest

@pytest.fixture()
def stock_sample():
    return stock.Stock('GOOG', 100, 490.1)

def test_create_stock(stock_sample):
    assert stock_sample.name == 'GOOG'
    assert stock_sample.shares == 100
    assert stock_sample.price == 490.1

def test_stock_cost(stock_sample):
    assert stock_sample.cost == 49010.0

def test_stock_raises_if_type_data_shares_is_not_int(stock_sample):
    with pytest.raises(TypeError):
        stock_sample.shares = '100'    

def test_stock_raises_if_type_data_name_is_not_str(stock_sample):
    with pytest.raises(TypeError):
        stock_sample.name = 100    

def test_stock_raises_if_type_data_price_is_not_float(stock_sample):
    with pytest.raises(TypeError):
        stock_sample.price = 100    

def test_selling_shares(stock_sample):
    stock_sample.sell(25)
    assert stock_sample.shares == 75