import os
from requests_oauthlib import OAuth1Session

TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

twitter = OAuth1Session(TWITTER_API_KEY,
                        client_secret=TWITTER_API_SECRET_KEY,
                        resource_owner_key=TWITTER_ACCESS_TOKEN,
                        resource_owner_secret=TWITTER_ACCESS_TOKEN_SECRET)

response = twitter.get('https://api.twitter.com/1.1/statuses/home_timeline.json')

for status in response.json():
    print('@' + status['user']['screen_name'], status['text'])
