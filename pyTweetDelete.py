'''pyTweetDelete - Delete your tweets from the command line.

Copyright (C) 2022 chrischriscris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

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
