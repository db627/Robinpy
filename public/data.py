from dotenv import load_dotenv
import os
import robin_stocks.robinhood as r

# Load environment variables using dotenv package
load_dotenv()

def stockNames(): #retrieves the names of stocks in my robinhood brokerage using robinhood api
    stock_data = r.account.build_holdings(with_dividends=False)
    return list(stock_data.keys())

def parseNames(stock_names): #parses the names of stocks in my robinhood brokerage using robinhood api
    return {name: getStockData(name) for name in stock_names}

def getStockData(stock_name): #retrieves the stock data of all my personal holdings using robinhood api
    return r.stocks.get_stock_historicals(stock_name, interval='hour', span='month', bounds='regular')

def format_stock_data(stock_data): #formats the stock data to be more readable and clean for the analysis
    result = []
    for symbol, data in stock_data.items(): #iterates through all teh stock data
        for entry in data: #for each stock, it cleans up the data to be more readable
            date = entry['begins_at'].split('T')[0]
            open_price = entry['open_price']
            close_price = entry['close_price']
            high_price = entry['high_price']
            low_price = entry['low_price']
            volume = entry['volume']
            session = entry['session']
            interpolated = entry['interpolated']

            result.append(f"Symbol: {symbol}, Date: {date}, Open Price: {open_price}, Close Price: {close_price}, High Price: {high_price}, Low Price: {low_price}, Volume: {volume}, Session: {session}, Interpolated: {interpolated}")
            #returns the data in a cleaner format
    return '\n'.join(result)

def moving_average(data, n): #uses a moving average strategy to analyze the data
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

def compute_rsi(data, window): #computes the rsi of each stock
    delta = [0] + [data[i] - data[i-1] for i in range(1, len(data))]
    gain = [delta[i] if delta[i] > 0 else 0 for i in range(len(delta))]
    loss = [-delta[i] if delta[i] < 0 else 0 for i in range(len(delta))]
    
    avg_gain = moving_average(gain, window)
    avg_loss = moving_average(loss, window)
    
    rs = []
    for i in range(len(avg_gain)):
        if avg_gain[i] is not None and avg_loss[i] is not None and avg_loss[i] != 0:
            rs.append(avg_gain[i] / avg_loss[i])
        else:
            rs.append(0)
    
    rsi = [100 - (100 / (1 + rs[i])) for i in range(len(rs))]
    
    return rsi

def analyzeData(cleaned_stock_data): #uses the moving average and rsi to predict when to buy sell and hold the stock
    actions = {}
    for symbol, data_entries in cleaned_stock_data.items():
        closing_prices = [float(entry['close_price']) for entry in data_entries]
        volumes = [int(entry['volume']) for entry in data_entries]

        if len(closing_prices) < 14:
            actions[symbol] = "hold"
            continue

        short_term_ma = moving_average(closing_prices, 5)
        long_term_ma = moving_average(closing_prices, 14)
        rsi = compute_rsi(closing_prices, 14)
        
        avg_volume = sum(volumes[-5:]) / 5

        if short_term_ma[-1] is not None and long_term_ma[-1] is not None and rsi[-1] is not None:
            if (short_term_ma[-2] <= long_term_ma[-2] and short_term_ma[-1] > long_term_ma[-1]) and rsi[-1] < 30 and volumes[-1] > avg_volume:
                actions[symbol] = "buy"
            elif (short_term_ma[-2] >= long_term_ma[-2] and short_term_ma[-1] < long_term_ma[-1]) and rsi[-1] > 70 and volumes[-1] > avg_volume:
                actions[symbol] = "sell"
            else:
                actions[symbol] = "hold"
        else:
            actions[symbol] = "hold"

    return actions

def organize_analyzed_data(analyzed_data): #organizes the predictions above and prepares them to be sent
    return '\n'.join([f"Symbol: {symbol}, Action: {action}" for symbol, action in analyzed_data.items()])


