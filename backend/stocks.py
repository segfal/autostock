import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


class Stock:
    def __init__(self,ticker):
        self.tick = ticker
        self.ticker = yf.Ticker(ticker)
        self.data = self.ticker.history(period="90d")
        self.data = self.data.reset_index()
        self.data = self.data.drop(columns=['Dividends', 'Stock Splits'])
        self.data = self.data.dropna()
        self.data = self.data.sort_values(by=['Date'])
        ##plot data
       

    
    def get_data(self):
        return self.data
    
    def get_timeseries(self):
        fig = px.line(self.data, x="Date", y="Close")
        fig.update_layout(title=f"{self.ticker.info['longName']}")
        return fig
    

    def get_returns(self):
        returns = self.data.Close.pct_change()
        return returns
    def get_mean_return(self):
        return self.get_returns().mean()
        










        





