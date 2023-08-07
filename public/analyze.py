from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
import robin_stocks.robinhood as r

# Load environment variables using dotenv package
load_dotenv()

# Connect langchain to the openAI API
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

def getStockData(stock_name):
    return r.stocks.get_stock_historicals(stock_name)

def stockNames():
    stock_data = r.account.build_holdings(with_dividends=False)
    return list(stock_data.keys())

def parseNames(stock_names):
    return {name: getStockData(name) for name in stock_names}

def format_stock_data(stock_data):
    result = []
    for symbol, data in stock_data.items():
        for entry in data:
            date = entry['begins_at'].split('T')[0]
            open_price = entry['open_price']
            close_price = entry['close_price']
            high_price = entry['high_price']
            low_price = entry['low_price']
            result.append(f"Symbol: {symbol}, Date: {date}, Open Price: {open_price}, Close Price: {close_price}, High Price: {high_price}, Low Price: {low_price}")
    return '\n'.join(result)

def moving_average(data, n):
    cumsum = [0]
    moving_avgs = []
    for i, x in enumerate(data, 1):
        cumsum.append(cumsum[i-1] + x)
        if i >= n:
            moving_avg = (cumsum[i] - cumsum[i-n]) / n
            moving_avgs.append(moving_avg)
        else:
            moving_avgs.append(None)
    return moving_avgs

def langchain(cleaned_stock_data):
    actions = {}
    for symbol, data_entries in cleaned_stock_data.items():
        closing_prices = [float(entry['close_price']) for entry in data_entries]

        # Use last 5 days of data
        closing_prices = closing_prices[-5:]

        if len(closing_prices) < 3:
            actions[symbol] = "hold"
            continue

        short_term_ma = moving_average(closing_prices, 2)
        long_term_ma = moving_average(closing_prices, 4)

        if short_term_ma[-1] is not None and long_term_ma[-1] is not None:
            if short_term_ma[-2] <= long_term_ma[-2] and short_term_ma[-1] > long_term_ma[-1]:
                actions[symbol] = "buy"
            elif short_term_ma[-2] >= long_term_ma[-2] and short_term_ma[-1] < long_term_ma[-1]:
                actions[symbol] = "sell"
            else:
                actions[symbol] = "hold"
        else:
            actions[symbol] = "hold"

    return actions

def organize_langchain(langchain_data):
    return '\n'.join([f"Symbol: {symbol}, Action: {action}" for symbol, action in langchain_data.items()])


