import pytest

def calculate_discount(prices, promo_codes):
    discounts = {
        'A': 0.1,
        'B': 0.2,
        'C': 0.3
    }
    total_price = sum(prices)
    promo_discount = 0
    for code in promo_codes:
        if code in discounts:
            promo_discount += total_price * discounts[code]
    return total_price - promo_discount

def test_calculate_discount():
    prices = [100, 200, 300]
    promo_codes = ['A', 'B']
    assert calculate_discount(prices, promo_codes) == 420.0

def test_calculate_discount_no_promo():
    prices = [100, 200, 300]
    promo_codes = []
    assert calculate_discount(prices, promo_codes) == 600.0

def test_calculate_discount_invalid_promo():
    prices = [100, 200, 300]
    promo_codes = ['D']
    assert calculate_discount(prices, promo_codes) == 600.0

def test_calculate_discount_empty_prices():
    prices = []
    promo_codes = ['A', 'B']
    assert calculate_discount(prices, promo_codes) == 0.0

def test_calculate_discount_empty_promo():
    prices = [100, 200, 300]
    promo_codes = []
    assert calculate_discount(prices, promo_codes) == 600.0
