import robin_stocks.robinhood as r

def login(user, pwd):
    r.login(username = user, password = pwd)