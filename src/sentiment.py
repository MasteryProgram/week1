import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_vader_sentiment(text):
    """Safe and robust VADER scorer - reinitializes if needed"""
    print("getting sentiment for:", text)
    if pd.isna(text) or not isinstance(text, str) or len(str(text).strip()) == 0:
        return {'compound': 0.0, 'pos': 0.0, 'neu': 0.0, 'neg': 0.0}
    
    try:
        # Create analyzer inside function (more reliable in notebooks)
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(str(text))
        print("scores:", scores)
        return scores
    except Exception as e:
        print(f"Error processing text: {e}")
        return {'compound': 0.0, 'pos': 0.0, 'neu': 0.0, 'neg': 0.0}


def add_sentiment_scores(df: pd.DataFrame, text_column: str = 'headline') -> pd.DataFrame:
    """Add VADER sentiment columns"""
    df = df.copy().reset_index(drop=True)
    print('why cant i see this?')
    
    print(f"Applying VADER to {len(df)} headlines...")
    sentiments = df[text_column].apply(get_vader_sentiment)
    sentiment_df = pd.DataFrame(sentiments.tolist())
    
    result = pd.concat([df, sentiment_df], axis=1)
    print("Sentiment scores added successfully.")
    return result


def categorize_sentiment(compound: float) -> str:
    if compound >= 0.05:
        return 'Positive'
    elif compound <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'


def aggregate_daily_sentiment(news_df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """Aggregate daily sentiment for one ticker"""
    df = news_df[news_df['stock'] == ticker].copy()
    
    if len(df) == 0:
        print(f"No news found for ticker: {ticker}")
        return pd.DataFrame()
    
    print(f"Processing {len(df)} articles for {ticker}...")
    
    # Add sentiment
    df = add_sentiment_scores(df)
    
    # Date handling
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
    df = df.dropna(subset=['date'])
    
    # Aggregate
    daily = df.groupby('date').agg({
        'compound': 'mean',
        'pos': 'mean',
        'neg': 'mean',
        'neu': 'mean',
        'headline': 'count'
    }).rename(columns={
        'compound': 'avg_sentiment',
        'headline': 'article_count'
    })
    
    daily['sentiment_category'] = daily['avg_sentiment'].apply(categorize_sentiment)
    
    print(f"✅ Successfully aggregated {len(daily)} trading days for {ticker}")
    return daily.reset_index()