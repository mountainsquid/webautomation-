#script that shows you today's date, time, days left in the year, current eth and btc price in real time

import datetime
import requests

current_date = datetime.datetime.now()
end_of_year = datetime.datetime(current_date.year, 12, 31)
days_left = (end_of_year - current_date).days



# grabs BTC's price 

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)

data = response.json()

price = data["bpi"]["USD"]["rate"]

# grabs eth price

url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"

response = requests.get(url)

data = response.json()

ethprice = data["ethereum"]["usd"]

# getting current time and date 

current_time = datetime.datetime.now().time()
current_date = datetime.datetime.now().date()

# printing stuff 

print("Beep bop. Script running...")
print("Current Time:", current_time)
print("Current Date:", current_date)
print("Days left in the year:", days_left)
print("Bitcoin Price: $" + price)
print("Ethereum Price: $" + str(ethprice))

