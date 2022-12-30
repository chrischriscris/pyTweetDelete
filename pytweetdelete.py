import argparse
import os
import csv
import tweepy
from dotenv import load_dotenv

def get_args():
    parser = argparse.ArgumentParser(
        description="Delete all the tweets that you don't like"
    )

    parser.add_argument(
        '-f',
        '--file',
        help='file to save the tweets to be deleted',
        default='deleted_tweets.csv',
        action='store',
    )

    parser.add_argument(
        '-l',
        '--likes',
        help='keep tweets with at least this many likes',
        default=float('inf'),
        action='store',
        type=int
    )

    parser.add_argument(
        '-r',
        '--rts',
        help='keep tweets with at least this many retweets',
        default=float('inf'),
        action='store',
        type=int
    )

    # Specify if append to the file
    parser.add_argument(
        '-a',
        '--append',
        help='append to the file',
        default=False,
        action='store_true'
    )

    return parser.parse_args()

def auth_twitter_app() -> tweepy.OAuth1UserHandler:
    '''Returns an authenticated tweepy API object'''
    load_dotenv()
    consumer_key = os.getenv('API_KEY')
    consumer_secret = os.getenv('API_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    return auth

def get_tweet_data(tweet: tweepy.models.Status) -> dict:
    '''Returns a dictionary with the tweet relevant data'''
    return {
        'id': tweet.id,
        'text': tweet.text,
        'date': tweet.created_at,
        'n_favs': tweet.favorite_count,
        'n_rts': tweet.retweet_count
    }

def main():
    args = get_args()
    auth = auth_twitter_app()
    api = tweepy.API(auth)

    # Check if credentials are valid
    try:
        api.user_timeline(count=1)
    except:
        print('Authentication failed. Check your credentials.')
        return

    # Overwrites the file if not appending specified
    with open(args.file, 'a' if args.append else 'w') as deleted_tweets_csv:
        header = ['text', 'date', 'n_favs', 'n_rts']

        tweet_writer = csv.DictWriter(
            deleted_tweets_csv,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
            fieldnames=header,
            extrasaction='ignore'
        )

        # Write header if not appending
        if not args.append:
            tweet_writer.writeheader()

        latest_tweet_id = api.user_timeline(count=1)[0].id

        # Loop until there are no more tweets satysfying the conditions
        while True:
            # Get tweets in batches of 200
            tl = api.user_timeline(
                count=200,
                max_id=latest_tweet_id,
            )

            if not tl:
                break

            latest_tweet_id = tl[-1].id

            for tweet in tl:
                tweet_data = get_tweet_data(tweet)

                # Delete tweet if it has less likes or less and less  retweets
                # than the specified
                if (tweet_data['n_favs'] < args.likes and
                    tweet_data['n_rts'] < args.rts):
                    # Write before destroy
                    tweet_writer.writerow(tweet_data)
                    api.destroy_status(tweet.id)

        print(f'Done! Deleted tweets saved to {args.file}')

if __name__ == '__main__':
    main()
