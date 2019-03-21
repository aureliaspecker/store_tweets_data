import requests
from requests_oauthlib import OAuth1

class TweetService:

    def __init__(self, twitter_credentials):
        self.twitter_credentials = twitter_credentials

    def get_tweet(self, tweet_id):

        url = 'https://api.twitter.com/1.1/statuses/show/{}.json'.format(tweet_id)
        auth = OAuth1(
            self.twitter_credentials.consumer_key, 
            self.twitter_credentials.consumer_secret, 
            self.twitter_credentials.token, 
            self.twitter_credentials.token_secret
        )
        headers = {'content-type': 'application/json'}

        result = requests.get(url, auth=auth, headers=headers)

        return result.json()