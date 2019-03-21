import requests
from requests_oauthlib import OAuth1

class UserService: 
    
    def __init__(self, twitter_credentials):
        self.twitter_credentials = twitter_credentials
    
    def get_user(self, user_id):

        parameters = {'user_id':'{}'.format(user_id)}
        headers = {'content-type': 'application/json'}
        auth = OAuth1(
            self.twitter_credentials.consumer_key, 
            self.twitter_credentials.consumer_secret, 
            self.twitter_credentials.token, 
            self.twitter_credentials.token_secret
        )

        result = requests.get('https://api.twitter.com/1.1/users/show.json', params=parameters, auth=auth, headers=headers)

        return result.json()