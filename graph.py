
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import numpy as np
import math

data = pd.read_csv("C:\Crypto_Data\BTC DATA 2015-2022 1D.csv")
x = [data['Close']]
y = list(range(1, 2565))

plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
