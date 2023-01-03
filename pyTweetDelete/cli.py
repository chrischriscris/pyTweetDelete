import argparse

def get_args():
    '''Parses the command line arguments'''
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

    parser.add_argument(
        '-u',
        '--unlike',
        help='unlike tweets',
        default=False,
        action='store_true'
    )

    return parser.parse_args()
