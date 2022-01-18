import yfinance as yf

class Stock:
	def __init__(self, stock_abbreviation):
		self.abbreviation = stock_abbreviation
		self.ticker = yf.Ticker(stock_abbreviation)
		self.info = self.ticker.info
		self.news = self.ticker.news
		self.history = self.ticker.history(period="max",interval="1mo")
		# possible parameter settings for <interval>:
		#	"1d"
		#	"1wk"
		#	"1mo"
		#	"1j"
		#	"ytd"
		#	"max"
		# print(hist["Open"], hist["Close"])

	def __str__(self):
		print(f"some info about {self.abbreviation}")


# for key, value in nvidia
# for news_item in nvidia.news:
	#print(news_item)
	# print(news_item["providerPublishTime"], news_item["title"], news_item["link"])

nvd = Stock("NVD")
print(nvd.info)


print(nvd.history)

