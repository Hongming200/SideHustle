import requests
import pandas as pd
import numpy as np
import tweepy
import configparser

#read config
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# # Get the top 50 crypto coins by market capitalization
# url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
# parameters = {"start": "1", "limit": "50", "convert": "USD"}
# headers = {"X-CMC_PRO_API_KEY": "YOUR_API_KEY_HERE"}
#
# response = requests.get(url, headers=headers, params=parameters)
# data = response.json()
#
# # Put the data into a pandas dataframe
# coins = pd.DataFrame(data["data"])
#
# # Calculate the RSI for each coin
# for coin in coins:
#     # Get the historical data for the coin
#     url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical?symbol={coin}&interval=daily&convert=USD"
#     historical_data = requests.get(url, headers=headers).json()["data"]
#     historical_data = pd.DataFrame(historical_data)
#
#     # Calculate the RSI
#     delta = historical_data["close"].diff()
#     gain = delta.where(delta > 0, 0)
#     loss = -delta.where(delta < 0, 0)
#     avg_gain = gain.rolling(14).mean()
#     avg_loss = loss.rolling(14).mean()
#     rs = avg_gain / avg_loss
#     rsi = 100 - (100 / (1 + rs))
#     coins.loc[coins["symbol"] == coin, "RSI"] = rsi
#
# # Find the coins that are overbought or oversold
# overbought = coins[coins["RSI"] > 70]
# oversold = coins[coins["RSI"] < 30]
#
# # Send an API to a twitter account and post it when the RSI indicates that a coin is overbought or oversold
# # Add your code here
