import pandas as pd
import talib


def compute_sma(series, window=20):
    return talib.SMA(series, timeperiod=window)


def compute_ema(series, window=20):
    return talib.EMA(series, timeperiod=window)


def compute_rsi(series, window=14):
    return talib.RSI(series, timeperiod=window)


def compute_macd(series):
    macd, signal, hist = talib.MACD(series)

    return pd.DataFrame({
        'MACD': macd,
        'Signal': signal,
        'Histogram': hist
    })


def get_daily_return(series):
    return series.pct_change() * 100