import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import yfinance as yf

def get_asset(tickers):
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        bs = comp.get_balance_sheet().T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = bs['Total Assets']
    return df

def get_liabilities(tickers):
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        bs = comp.get_balance_sheet().T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = bs['Total Liab']
        
    return df

def get_equity(tickers):
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        bs = comp.get_balance_sheet().T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = bs['Total Assets']-bs['Total Liab']
        
    return df


def get_revenue(tickers):
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        financials = comp.get_financials().T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = financials['Total Revenue']
    return df

def get_ROE(tickers):
    
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        financials = (comp.get_financials()).T
        bs = (comp.get_balance_sheet()).T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
        
        df[ticker] = financials['Net Income']/(bs['Total Assets'] - bs['Total Liab'])
        
    return df

def get_ROA(tickers):
    
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        financials = (comp.get_financials()).T
        bs = (comp.get_balance_sheet()).T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
        
        df[ticker] = financials['Net Income']/bs['Total Assets']
        
    return df

def get_NPM(tickers):
    
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        financials = (comp.get_financials()).T
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = financials['Net Income']/financials['Total Revenue']
        
    return df

def get_asset_turnover(tickers):
    
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        financials = (comp.get_financials()).T
        bs = (comp.get_balance_sheet()).T
        
        
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = financials['Total Revenue']/bs['Total Assets']
        
    return df

def get_financial_leverage(tickers):
    
    for ticker in tickers:
        comp = yf.Ticker(ticker)
        bs = (comp.get_balance_sheet()).T
             
        if ticker == tickers[0]:
            df = pd.DataFrame()
            
        df[ticker] = bs['Total Assets']/(bs['Total Assets']-bs['Total Liab'])
        
    return df


def plot_time_series(data, title, figsize):
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title, size=20)

    for col in data.columns:
        ax.plot(data[col], label=col)
        for index in range(len(data.index)):
            ax.text(x=data.index[index], y=data[col][index], s=np.round(data[col][index], 2), size=12)

    ax.legend()        
    ax.set_xticks(data.index, size=12)
    ax.grid()