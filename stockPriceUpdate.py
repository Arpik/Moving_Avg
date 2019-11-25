# import bs4
# import requests
# from bs4 import BeautifulSoup
# import threading


# def parsePrice():
#     r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
#     soup = bs4.BeautifulSoup(r.text, "lxml")
#     price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
#     threading.Timer(10.0, parsePrice).start()
#     print(price)

# parsePrice()
# while True:
#     print('The current price:' + str(parsePrice()))

# import bs4
# import requests
# from bs4 import BeautifulSoup
# import threading
# import queue

# def parsePrice():
#     r = requests.get('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD')
#     soup = bs4.BeautifulSoup(r.text, "lxml")
#     price = soup.find_all('div', {'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'})[0].find('span').text
#     return price 
    

# def add_to_list():
#     price_list = []
#     for _ in range(1,11):
#        current_price = parsePrice()
#        current_price = current_price.replace(',', '')
#        price_list.append(float(current_price))
#         # price_list.append(threading.Timer(5.0, parsePrice).start())
#     return (price_list)

# def avg(mlist):
#     return sum(mlist) / len(mlist)

# my_list = add_to_list()

# print(avg(my_list))




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





# def add_to_list():
#     price_list = []
#     current_price = threading.Timer(1.0, parsePrice).start()
#     print(current_price)
    
    # price_list.append(current_price)
    # if len(price_list) == 10:
    #     current_price.cancel()
        
    # # print(soup.title.name)
    # for i in range(len(price_list)):
    #     print(price_list[i])
# def get_price():
# add_to_list()

# get_price()
