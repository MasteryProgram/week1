import pandas as pd
import talib
import pynance as pn   # We'll use it for extra utilities


def compute_sma(series, window=20):
    """Simple Moving Average"""
    return talib.SMA(series, timeperiod=window)


def compute_ema(series, window=20):
    """Exponential Moving Average"""
    return talib.EMA(series, timeperiod=window)


def compute_rsi(series, window=14):
    """Relative Strength Index"""
    return talib.RSI(series, timeperiod=window)


def compute_macd(series):
    """MACD, Signal Line, and Histogram"""
    macd, signal, hist = talib.MACD(series)
    return pd.DataFrame({
        'MACD': macd,
        'Signal': signal,
        'Histogram': hist
    })


def compute_bollinger_bands(series, window=20, nbdev=2):
    """Bollinger Bands"""
    upper, middle, lower = talib.BBANDS(
        series, 
        timeperiod=window, 
        nbdevup=nbdev, 
        nbdevdn=nbdev
    )
    return pd.DataFrame({
        'BB_Upper': upper,
        'BB_Middle': middle,
        'BB_Lower': lower
    })


def compute_atr(high, low, close, window=14):
    """Average True Range"""
    return talib.ATR(high, low, close, timeperiod=window)


def get_daily_return(series):
    """Daily percentage return"""
    return series.pct_change() * 100


# ====================== pynance utilities ======================
def pn_stock_info(ticker: str):
    """Get stock info using pynance"""
    return pn.stocks.get(ticker)


def add_pynance_features(df: pd.DataFrame):
    """
    Optional: Add extra features from pynance if useful
    (mainly for data fetching / some derived metrics)
    """
    df = df.copy()
    # Example: You can use pynance for other calculations if needed
    return df


def add_all_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Master function - Adds all indicators at once
    Expects columns: Open, High, Low, Close, Volume
    """
    df = df.copy()
    
    # TA-Lib indicators
    df['SMA_20'] = compute_sma(df['Close'], 20)
    df['EMA_20'] = compute_ema(df['Close'], 20)
    df['RSI'] = compute_rsi(df['Close'])
    
    macd_df = compute_macd(df['Close'])
    bb_df = compute_bollinger_bands(df['Close'])
    
    df = df.join(macd_df)
    df = df.join(bb_df)
    
    df['ATR'] = compute_atr(df['High'], df['Low'], df['Close'])
    df['Daily_Return'] = get_daily_return(df['Close'])
    df['Volatility_20'] = df['Daily_Return'].rolling(window=20).std()
    
    return df