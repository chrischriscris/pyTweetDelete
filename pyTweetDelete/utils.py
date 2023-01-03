'''utils.py - Utility functions for pyTweetDelete.

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