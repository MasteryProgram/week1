import pandas as pd
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose


def rolling_statistics(series, window=12):
    rolling_mean = series.rolling(window).mean()
    rolling_std = series.rolling(window).std()

    return rolling_mean, rolling_std


def decompose_series(series, period=12):
    return seasonal_decompose(
        series,
        model='additive',
        period=period
    )


def adf_test(series):
    result = adfuller(series.dropna())

    return {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Critical Values': result[4]
    }