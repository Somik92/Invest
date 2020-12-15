import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def option(type, premium, strike, expiration_price):
    if type == 'call':
        if expiration_price == strike or expiration_price < strike:
            pl = premium
        elif expiration_price > strike:
            pl = premium + (strike - expiration_price)
    elif type == 'put':
        if expiration_price == strike or expiration_price > strike:
            pl = premium
        elif expiration_price < strike:
            pl = premium + (expiration_price - strike)
    return pl
def option_spread(type, sell_premium, sell_strike, buy_premium, buy_strike, expiration_price):
        pl = option(type, sell_premium, sell_strike, expiration_price) \
             - option(type, buy_premium, buy_strike, expiration_price)
        return pl
def covered_call(spot, premium, strike, expiration_price):
    if strike > expiration_price or strike == expiration_price:
        pl = premium + (expiration_price - spot)
    elif strike < expiration_price:
        pl = premium + (strike - spot)
    return pl

def strike(first_strike, second_strike):
    strikes = []
    for i in np.arange(first_strike, second_strike, 0.1).tolist():
        theoretical_fx_rates =  np.round(i, 2)
        strikes.append(theoretical_fx_rates)
    return strikes

def strategy(quantity):
    for theoretical_fx_rate in strike(71000, 77000):
        pl = covered_call(75000, 423, 76000, theoretical_fx_rate) * quantity
        return pl


print(strategy(15))


