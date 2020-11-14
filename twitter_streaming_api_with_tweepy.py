import os
import tweepy


TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

def main():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    stream = tweepy.Stream(auth, MyStreamListener())

    stream.sample(languages=['ja'])

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status: tweepy.Status):
        print('@' + status.author.screen_name, status.text)

if __name__ == '__main__':
    main()
