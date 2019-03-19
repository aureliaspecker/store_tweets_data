import requests
from requests_oauthlib import OAuth1

class Tweet:

    def __init__(self):

        with open("credentials_2.txt", "r") as file_2: 
            consumer_key = file_2.readline().split()[2]
            consumer_secret = file_2.readline().split()[2] 
            token = file_2.readline().split()[2] 
            token_secret = file_2.readline().split()[2]

        url = 'https://api.twitter.com/1.1/statuses/show/1106982589179576320.json'
        auth = OAuth1(consumer_key, consumer_secret, token, token_secret)
        headers = {'content-type': 'application/json'}

        r = requests.get(url, auth=auth, headers=headers)

        print(r.text)

Tweet()