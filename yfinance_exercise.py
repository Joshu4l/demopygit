import yfinance as yf

nvidia = yf.Ticker("NVD")

# get stock info
print(nvidia.info)
print(type(nvidia.info))

# get historical market data
hist = nvidia.history(period="max")
