import robin_stocks.robinhood as r

def login(user, pwd): #connects to robinhood account
    r.login(username = user, password = pwd)

def simplify_stock_data(): #cleans up the stock data to be more readable
    stock_data = r.account.build_holdings(with_dividends=False)
    simplified_data = ""
    for key, value in stock_data.items():
        price = "{:.2f}".format(float(value['price'])) # format as 2 decimal places
        quantity = "{:.8f}".format(float(value['quantity'])) # format as 8 decimal places
        equity = "{:.2f}".format(float(value['equity'])) # format as 2 decimal places
        simplified_data += f"Stock: {key}\nPrice: {price}\nQuantity: {quantity}\nEquity: {equity}\n\n"
    return simplified_data

def viewAccountInfo(): #pulls account info from robinhood account
    my_stocks = r.build_holdings()
    for key,value in my_stocks.items():
        print(key,value)
    my_portfolio = r.profiles.load_portfolio_profile(info=("market_value"))
    my_info = r.account.build_holdings(with_dividends = False)
    for value in my_portfolio:
        print(value)
    print(my_info)

