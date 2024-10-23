import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets["content"] = tweets["content"].apply(lambda x: int(len(x)))
    return tweets.loc[(tweets["content"] > 15), "tweet_id"].to_frame()
    