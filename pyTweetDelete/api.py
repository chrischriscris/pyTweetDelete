import csv
import os

import tweepy
from dotenv import load_dotenv

from pyTweetDelete.utils import get_tweet_data

MAX_TWEETS_PER_REQUEST=200

def auth_twitter_app() -> tweepy.OAuth1UserHandler:
    '''Returns an authenticated tweepy API object using the credentials in the
    .env file (API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    :return: authenticated tweepy API object
    '''
    load_dotenv()
    consumer_key = os.getenv('API_KEY')
    consumer_secret = os.getenv('API_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth= tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    api = tweepy.API(auth)

    # Check if credentials are valid
    try:
        api.user_timeline(count=1)
    except:
        raise ValueError('Authentication failed. Check your credentials.')

    return api

def delete_tweets(
    filename: str,
    api: tweepy.API,
    min_likes: int,
    min_rts: int
):
    '''Deletes tweets and saves them to a csv file

    :param filename: name of the file to save the tweets to be deleted
    :param api: authenticated tweepy API object
    :param min_likes: keep tweets with at least this many likes
    :param min_rts: keep tweets with at least this many retweets
    '''
    with open(filename, 'a') as deleted_tweets_csv:
        header = ['text', 'date', 'n_favs', 'n_rts']

        tweet_writer = csv.DictWriter(
            deleted_tweets_csv,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
            fieldnames=header,
            extrasaction='ignore'
        )

        tweet_writer.writeheader()

        latest_tweet_id = api.user_timeline(count=1)[0].id
        
        # Loop until there are no more tweets satysfying the conditions
        while True:
            # Get tweets in batches
            tl = api.user_timeline(
                count=MAX_TWEETS_PER_REQUEST,
                max_id=latest_tweet_id,
            )

            if not tl:
                break

            latest_tweet_id = tl[-1].id

            for tweet in tl:
                tweet_data = get_tweet_data(tweet)

                # Delete tweet if it has less likes or less and less  retweets
                # than the specified
                if (tweet_data['n_favs'] < min_likes and
                    tweet_data['n_rts'] < min_rts):
                    # Write before destroy
                    tweet_writer.writerow(tweet_data)
                    api.destroy_status(tweet.id)

def unlike_tweets(api: tweepy.API):
    '''Unlikes all the tweets in the authenticated user's timeline

    :param api: authenticated tweepy API object
    '''
    latest_tweet_id = api.get_favorites(count=1)[0].id

    # Loop until there are no more tweets satysfying the conditions
    while True:
        # Get tweets in batches
        tl = api.get_favorites(
            count=MAX_TWEETS_PER_REQUEST,
            max_id=latest_tweet_id,
            include_entities=False
        )

        if not tl:
            break

        latest_tweet_id = tl[-1].id

        for tweet in tl:
            api.destroy_favorite(tweet.id)