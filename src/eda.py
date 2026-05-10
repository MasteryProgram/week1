from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def headline_length_stats(df, column='headline'):
    lengths = df[column].str.len()

    return lengths.describe()


def publisher_counts(df, column='publisher'):
    return df[column].value_counts()


def article_frequency_over_time(df, date_column='date'):
    return df.groupby(df[date_column].dt.date).size()


def extract_common_keywords(text_series, top_n=20):
    vectorizer = CountVectorizer(stop_words='english')

    X = vectorizer.fit_transform(text_series)

    word_counts = X.sum(axis=0)

    words_freq = [
        (word, word_counts[0, idx])
        for word, idx in vectorizer.vocabulary_.items()
    ]

    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

    return words_freq[:top_n]