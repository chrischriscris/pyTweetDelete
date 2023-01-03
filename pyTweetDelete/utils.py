import tweepy

def get_tweet_data(tweet: tweepy.models.Status) -> dict:
    '''Returns a dictionary with the tweet relevant data'''
    return {
        'id': tweet.id,
        'text': tweet.text,
        'date': tweet.created_at,
        'n_favs': tweet.favorite_count,
        'n_rts': tweet.retweet_count
    }