import yfinance as yf

class Stock:
	def __init__(self, stock_abbreviation):
		self.abbreviation = stock_abbreviation
		self.ticker = yf.Ticker(stock_abbreviation)
		self.info = self.ticker.info
		self.news = self.ticker.news
		self.available_history_data = [col for col in self.ticker.history().columns]
		self.history_all = self.ticker.history(period="max",interval="1d",start="2007-12-01")
		# possible parameter settings for <interval>:
		#	"1d"
		#	"1wk"
		#	"1mo"
		#	"1j"
		#	"ytd"
		#	"max"
		# print(hist["Open"], hist["Close"])

	def __str__(self):
		return f"{self.abbreviation}'s general information:\n" \
			   f"{self.info}\n"

	def get_history_specified(self, start, interval):

		hist = self.ticker.history(period="max", start=start, interval=interval)
		if len(hist) > 0:
			return hist
		else:
			return f"no entry found for the specified search parameters"

msft = Stock("MSFT")

print(msft)

print(f"available history data:\n{msft.available_history_data}\n")
print(msft.history_all)
# print(msft.get_history_specified("2007-01-01", "1wk"))