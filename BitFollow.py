from urllib.request import urlopen
import time
from termcolor import colored

cval = 0
color = ""
startprice = 0

def getstartprice():
    global startprice
    response = urlopen('https://blockchain.info/tobtc?currency=TRY&value=100')
    html_doc = response.read()
    html_doc = html_doc.decode('utf-8')
    startprice = int(100/(float(html_doc)))

def pricecalc():
    global cval, color
    response = urlopen('https://blockchain.info/tobtc?currency=TRY&value=100')
    html_doc = response.read()
    html_doc = html_doc.decode('utf-8')
    price = int(100/(float(html_doc)))
    nval = price
    if(nval > cval):
        cval = nval
        color = "green"
        print(colored(price, color) , "Net difference of" , (nval - startprice))
    elif(nval == cval):
        cval = nval
        print(colored(price, color) , "Net difference of" , (nval - startprice))
    else:
        cval = nval
        color = "red"
        print(colored(price, color) , "Net difference of" , (nval - startprice))

getstartprice()
while(True):
    pricecalc()
    time.sleep(30)
