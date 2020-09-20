import requests
import bs4
import pandas as pd

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
offer = []

def tracker(url, TrackingPrice):
    res = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(res.content, features='lxml')

    # Prevent crash when price isn't available
    try:
        title = soup.find(id='productTitle').get_text().strip()
        amount = float(soup.find(id='priceblock_ourprice').get_text().replace("$", "").strip())
        if amount <= TrackingPrice:
            offer.append("You got an offer on the {0} for {1}. Check out the product {2}".format(title, amount, url))
        
    except:
        offer.append("Couldn't get details about product.")


df = pd.read_csv("ProductList.csv")
for i in range(0, len(df["URL"])):
    tracker(df["URL"][i], df["TrackingPrice"][i])

outputs["message"]=offer

