import matplotlib.pyplot as plt


def plot_price_and_sma(df, price_col='Close', sma_col='SMA_20'):
    plt.figure(figsize=(12, 5))

    plt.plot(df.index, df[price_col], label='Close')
    plt.plot(df.index, df[sma_col], label=sma_col)

    plt.legend()
    plt.title('Price vs SMA')

    plt.show()


def plot_rsi(df, rsi_col='RSI'):
    plt.figure(figsize=(12, 4))

    plt.plot(df.index, df[rsi_col])

    plt.axhline(70, linestyle='--')
    plt.axhline(30, linestyle='--')

    plt.title('RSI')

    plt.show()