import requests
from requests_oauthlib import OAuth1

class User: 
    
    def __init__(self):
    
        with open("credentials_2.txt", "r") as file_2: 
            consumer_key = file_2.readline().split()[2]
            consumer_secret = file_2.readline().split()[2] 
            token = file_2.readline().split()[2] 
            token_secret = file_2.readline().split()[2]

        parameters = {'user_id':'1062705508400971776'}
        headers = {'content-type': 'application/json'}
        auth = OAuth1(consumer_key, consumer_secret, token, token_secret)

        r = requests.get('https://api.twitter.com/1.1/users/show.json', params=parameters, auth=auth, headers=headers)

        print(r.text)

User()