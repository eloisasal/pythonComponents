#This is an example of a crypto tracker done only with copilot in 21/10/2022
#It's not perfect, but it's a good start

import copilot

#reads from binance api the value of a given crypto with a given currency
#returns the string with the current value, currency and the actual time
def get_crypto_value(crypto, currency):
    #get data from binance api
    data = copilot.read_json("https://api.binance.com/api/v3/ticker/price?symbol="+crypto+currency)
    #get current value
    value = data["price"]
    #get current time
    time = copilot.get_time()
    #return string with current value, currency and the actual time
    return value+currency+" at "+time

get_crypto_value("BTC","EUR")