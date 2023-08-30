import os
from message import sendMessage
from message import send_time_message
from login import login
from robin import simplify_stock_data
from dotenv import load_dotenv, dotenv_values
from data import getStockData, stockNames, parseNames, format_stock_data, analyzeData, organize_analyzed_data
class Main:
    load_dotenv()
    def main():
        try:
            user = os.getenv("ROBIN_USER")
            pwd = os.getenv("ROBIN_PASSWORD")
            if not user or not pwd:
                raise ValueError("Environment variables not set.")
        except Exception as e:
            print("Error reading environment variables:", str(e))
            user = input("Enter Robinhood username: ")
            pwd = input("Enter Robinhood password: ")
        login(user, pwd)
        print('Log in complete')
        stock_data = simplify_stock_data()
        # print(stock_data)
        stock_name = stockNames()
        raw_data = parseNames(stock_name)
        formatted_data = format_stock_data(raw_data)
        print(organize_analyzed_data(analyzeData(parseNames(stockNames()))))
        #send_time_message(str(stock_data) + '\n' + str(organize_langchain(langchain(parseNames(stockNames())))))
        sendMessage(str(stock_data) + '\n' + str(organize_analyzed_data(analyzeData(parseNames(stockNames())))))
        #print("Message sent!")
        

    if __name__ == "__main__":
        main()