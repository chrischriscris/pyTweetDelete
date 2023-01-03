'''cli.py - Command line interface for pyTweetDelete.

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
