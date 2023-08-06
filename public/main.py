import os
from message import sendMessage
from message import send_time_message
from login import login
from robin import simplify_stock_data
from dotenv import load_dotenv, dotenv_values
from analyze import getStockData, stockNames, parseNames, format_stock_data, langchain, organize_langchain

class Main:
    load_dotenv()
    def main():
        user = os.getenv("GET_ROBIN_PASS")
        pwd = os.getenv("ROBIN_PASSWORD")
        login(user, pwd)
        print('Log in complete')
        stock_data = simplify_stock_data()
        # print(stock_data)
        stock_name = stockNames()
        raw_data = parseNames(stock_name)
        formatted_data = format_stock_data(raw_data)
        print(organize_langchain(langchain(parseNames(stockNames()))))
        send_time_message(str(stock_data) + '\n' + str(organize_langchain(langchain(parseNames(stockNames())))))
        # sendMessage(str(stock_data) + '\n' + str(organize_langchain(langchain(parseNames(stockNames())))))
        print("Message sent!")
        

    if __name__ == "__main__":
        main()