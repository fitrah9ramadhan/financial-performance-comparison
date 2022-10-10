import requests

from bs4 import BeautifulSoup


def get_nth_biggest(n):

    page = requests.get("https://id.tradingview.com/markets/stocks-indonesia/market-movers-large-cap/")

    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find_all("table", {'class':'table-DR3mi0GH'})
    a = soup.find_all("a", {'class':'apply-common-tooltip tickerName-hMpTPJiS'})
    
    n_biggest_cap = []
    for i in a:
        n_biggest_cap.append(i.text)
        
    return n_biggest_cap[:n]