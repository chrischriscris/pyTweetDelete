from pyTweetDelete.api import auth_twitter_app, delete_tweets, unlike_tweets
from pyTweetDelete.cli import get_args


def main():
    args = get_args()

    try:
        api = auth_twitter_app()
    except ValueError as e:
        print(e)
        return

    if args.unlike:
        print('Unliking tweets...')
        unlike_tweets(api)
        print('Done!')
    else:
        print('Deleting tweets...')
        delete_tweets(args.file, api, args.likes, args.rts)
        print(f'Done! Deleted tweets saved to {args.file}')

if __name__ == '__main__':
    main()
