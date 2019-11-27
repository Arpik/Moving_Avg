import bs4
import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd
import queue

def get_price():
    r = requests.get('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD')
    soup = bs4.BeautifulSoup(r.text, "lxml")
    price = soup.find_all('div', {'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'})[0].find('span').text
    return price

    
def get_moving_avg():
    price_list = []
    for _ in range(0,10):
       current_price = get_price()
       current_price = current_price.replace(',', '')
       price_list.append(float(current_price))
       data_frame = pd.DataFrame(price_list)
       mov_avg_list = data_frame.rolling(3).mean()

        # price_list.append(threading.Timer(5.0, get_price).start())
    
    return (mov_avg_list)

# def avg(mlist):
#     return sum(mlist) / len(mlist)


my_list = get_moving_avg()

print(my_list)


