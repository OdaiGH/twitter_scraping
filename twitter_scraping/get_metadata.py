import tweepy
import math
from time import sleep
import json
from twitter_scraping.database import *

def get_tweets(user):
    with open('twitter_scraping/api_keys.json') as f:
        keys = json.load(f)

    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    api = tweepy.API(auth)
    user = user.lower()

    with open('tweets_ids/all_ids_for_{}.json'.format(user)) as f:
        ids = json.load(f)

    print('total ids: {}'.format(len(ids)))

    all_data = []
    start = 0
    end = len(ids)
    if len(ids) >=100:
        start = 0
        end = 100
    limit = len(ids)
    i = math.ceil(limit / 100)
    for go in range(i):
        print('currently getting {} - {}'.format(start, end))
        sleep(6)  # needed to prevent hitting API rate limit
        id_batch = ids[start:end]
        start += 100
        end += 100
        tweets = api.statuses_lookup(id_batch)
        for tweet in tweets:
            all_data.append(dict(tweet._json))

    return all_data        