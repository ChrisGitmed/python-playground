from datetime import date, timedelta
from matplotlib import pyplot as plt
from pandas import DataFrame
from yfinance import download
#Importing the necessary libraries

#establishing the start and end timeframes. Using timedelta allows the program to automatically update
#the timeframe (1 year from today, etc.) instead of having the user manually update each time
start = date.today() - timedelta(days=365) #timeframe = 1 year from today
start.strftime('%Y-%m-%d') #formatting to allow it to be read by the python program

end = date.today() + timedelta(2) #setting end date for today
end.strftime('%Y-%m-%d')

def Closing_Price(ticker): #creating this function allows me to access multiple tickers without repeating code
    asset = DataFrame(download(ticker, start=start, end=end)['Adj Close']) #retrieve the data from yf finance, set start and end date, only show closing price
    return asset #return data

TESLA=Closing_Price('TSLA') #tickers that can be called with the above function
NVIDIA=Closing_Price('NVDA')
VERIZON=Closing_Price('VZ')

#Creating the charts to display the data
plt.plot(TESLA, color='blue', label='TSLA')
plt.plot(NVIDIA, color='red', label='NVDA')
plt.plot(VERIZON, color='green', label='VZ')
plt.title('Stock Price History')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
leg = plt.legend(loc='upper left')
plt.show()

