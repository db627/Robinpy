from dotenv import load_dotenv, dotenv_values
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import robin_stocks.robinhood as r

# load enviornment variables using dotenv package
load_dotenv()

#connect langchain to the openAI api
llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"))
# get stock data using robinstocks
def getStockData(stock_name):
    my_stocks = r.stocks.get_stock_historicals(str(stock_name))
    return my_stocks

# get stock data from my account. Loop through dictionary and get the keys (symbols) of my stocks
def stockNames():
    stock_data = r.account.build_holdings(with_dividends=False)
    stock_names = []
    for key, value in stock_data.items():
        stock_names.append(key)
    return stock_names

# using the names of my stocks, get the data for each stock
def parseNames(stock_names):
    info = {}
    for name in stockNames():
        info[str(name)] = (getStockData(name))
    return info

#format the data into a clean sentance sorting everything by stock
def format_stock_data(stock_data):
    result = []
    for symbol, data in stock_data.items():
        for entry in data:
            date = entry['begins_at'].split('T')[0]
            open_price = entry['open_price']
            close_price = entry['close_price']
            high_price = entry['high_price']
            low_price = entry['low_price']
            line = f"Symbol: {symbol}, Date: {date}, Open Price: {open_price}, Close Price: {close_price}, High Price: {high_price}, Low Price: {low_price}"
            result.append(line)
    return '\n'.join(result)

#use that data to predict if to buy or sell the stock
def langchain(cleaned_stock_data):
    actions = {}
    for symbol, data_entries in cleaned_stock_data.items():
        data_string = f"Symbol: {symbol}"
        for entry in data_entries:
            date = entry['begins_at'].split('T')[0]
            open_price = entry['open_price']
            close_price = entry['close_price']
            high_price = entry['high_price']
            low_price = entry['low_price']
            data_string += f", Date: {date}, Open Price: {open_price}, Close Price: {close_price}, High Price: {high_price}, Low Price: {low_price}"
        if float(data_entries[-1]['close_price']) > float(data_entries[0]['open_price']):
            action = "buy"
        elif float(data_entries[-1]['close_price']) < float(data_entries[0]['open_price']):
            action = "sell"
        else:
            action = "hold"

        actions[symbol] = action
    
    return actions

# organize the predictions from a dictionary to strings
def organize_langchain(langchain_data):
    result = []
    for symbol, action in langchain_data.items():
        line = f"Symbol: {symbol}, Action: {action}"
        result.append(line)
    return '\n'.join(result)
