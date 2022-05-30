import yfinance as yf
import pandas as pd
import numpy as np




class Stock:
    def __init__(self,ticker):
        self.ticker = yf.Ticker(ticker)
        





