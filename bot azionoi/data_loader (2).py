import yfinance as yf 
import pandas as pd 
from config import LOG_FILE, LOG_FOLDER, TICKER, START_DATE, END_DATE, FAST_MA, SLOW_MA

def load_data():
    '''
    scarica i dati  storici del tiker configurato

    '''
    data =yf.download(TICKER, start=START_DATE, end=END_DATE)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns=data.columns.get_level_values(0)
        
    data = data.dropna().copy()
    return data


def create_features(data):

    '''
    creiamo le feature principali x la strategia
    '''
    
    df=data.copy()
    
    df['Return']=df['Close'].pct_change()
    df['MA_FAST']=df['Close'].rolling(FAST_MA).mean()
    df['MA_SLOW']=df['Close'].rolling(SLOW_MA).mean()
    df["Momentum_5"]=df["Close"]/df['Close'].shift(5)-1
    df['Volatility_10']=df["Return"].rolling(10).std()
    
    df=df.dropna().copy()
    return df












    