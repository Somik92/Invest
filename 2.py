import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# def for net premium of spreads
def my_strategy_sell_option_call_spread_premium(price_sell_call, price_buy_call):
    premium = (price_sell_call - price_buy_call)
    return premium
def my_strategy_sell_option_put_spread_premium(price_sell_put, price_buy_put):
    premium = (price_sell_put - price_buy_put)
    return premium
# def for pl of spreads
def my_strategy_sell_option_call_spread_PL(call_prem_sell, call_prem_buy,theoretical_spot_rate_expiration, quantity, sell_call_strike, buy_call_strike):
    if theoretical_spot_rate_expiration == sell_call_strike or theoretical_spot_rate_expiration < sell_call_strike:
        pl = my_strategy_sell_option_call_spread_premium(call_prem_sell, call_prem_buy) * quantity
    elif theoretical_spot_rate_expiration == buy_call_strike or theoretical_spot_rate_expiration > buy_call_strike:
        pl = my_strategy_sell_option_call_spread_premium(call_prem_sell, call_prem_buy) * quantity + ((sell_call_strike * 1000 - buy_call_strike * 1000) * quantity)
    elif theoretical_spot_rate_expiration > sell_call_strike and theoretical_spot_rate_expiration < buy_call_strike:
        pl = my_strategy_sell_option_call_spread_premium(call_prem_sell, call_prem_buy) * quantity + ((sell_call_strike * 1000 - theoretical_spot_rate_expiration * 1000) * quantity)

    return pl
def my_strategy_sell_option_put_spread_PL(put_prem_sell, put_prem_buy, theoretical_spot_rate_expiration, quantity, sell_put_strike, buy_put_strike):
    if theoretical_spot_rate_expiration == sell_put_strike or theoretical_spot_rate_expiration > sell_put_strike:
        pl = my_strategy_sell_option_put_spread_premium(put_prem_sell, put_prem_buy) * quantity
    elif theoretical_spot_rate_expiration == buy_put_strike or theoretical_spot_rate_expiration < buy_put_strike:
        pl = my_strategy_sell_option_call_spread_premium(put_prem_sell, put_prem_buy) * quantity + ((buy_put_strike* 1000 - sell_put_strike * 1000) * quantity)
    elif theoretical_spot_rate_expiration < sell_put_strike and theoretical_spot_rate_expiration > buy_put_strike:
        pl = my_strategy_sell_option_call_spread_premium(put_prem_sell, put_prem_buy) * quantity + ((theoretical_spot_rate_expiration * 1000 - sell_put_strike * 1000) * quantity)
    return pl
# tech def for np.array of strikes
def strike(first_strike, second_strike):
    strikes = []
    for i in np.arange(first_strike, second_strike, 0.1).tolist():
        theoretical_fx_rates =  np.round(i, 2)
        strikes.append(theoretical_fx_rates)
    return strikes
# def for pl for graph
def pl(first_strike, second_strike):
    df = []
    for theoretical_fx_rate in strike(first_strike, second_strike):
        df.append({'strike': theoretical_fx_rate, 'PL': my_strategy_sell_option_put_spread_PL(put_prem_sell=423, put_prem_buy=287, theoretical_spot_rate_expiration=theoretical_fx_rate,
                                                                                               quantity=15, sell_put_strike=75, buy_put_strike=74.5) +
                                                        my_strategy_sell_option_call_spread_PL(call_prem_sell=423, call_prem_buy=287, theoretical_spot_rate_expiration=theoretical_fx_rate,
                                                                                               quantity=15, sell_call_strike=76, buy_call_strike=76.5)})
    df = pd.DataFrame(df)
    df = df[['strike', 'PL']]
    return df




start_strike = 71
end_strike = 82
step = 1


strikes_for_graph = pl(start_strike, end_strike)['strike']
pl_for_graph = pl(start_strike, end_strike)['PL']
plt.plot(strikes_for_graph, pl_for_graph)
plt.xticks(np.arange(start_strike, end_strike, step))
plt.ylabel('P&L')
plt.show()




