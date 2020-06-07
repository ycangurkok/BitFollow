from urllib.request import urlopen
import time

def pricecalc():
    response = urlopen('https://blockchain.info/tobtc?currency=TRY&value=100')
    html_doc = response.read()
    html_doc = html_doc.decode('utf-8')
    price = 100/(float(html_doc))
    print(int(price))

while(True):
    pricecalc()
    time.sleep(5)
