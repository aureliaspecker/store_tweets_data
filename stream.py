import subprocess
import json
import threading

class Stream: 


    def __init__(self, **kwargs):
        """Initialise stream connection with bearer token, account name and stream (prod, dev)"""

        #Unpack user credentials from dictionary
        token = kwargs.get("bearer_token")
        account_name = kwargs.get("account_name")
        stream_name = kwargs.get("stream_name")

        #Run curl command
        curl_command = ['curl','-v','-H','Authorization:Bearer {}'.format(token), '-H', 'content-type:application/json', '-X', 'GET', 'https://data-api.twitter.com/stream/insightstrack/accounts/{}/publishers/twitter/{}.json?backfillMinutes=2'.format(account_name, stream_name)]
        self.popen = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=False) 
        
        #Monitor stream in background
        thread = threading.Thread(target=self.track, args=())
        thread.daemon = True
        thread.start()


    def track(self):
        """Monitor stream and store engagement data"""

        self.engagement_data = []
        self.unsynced_data = 0
        while True:
            line = self.popen.stdout.readline()
            if line is not None and line != '':
                try:
                    eng_data = json.loads(line)
                    self.engagement_data.append(eng_data)
                    self.unsynced_data += 1
                except ValueError:
                    pass


    def get_engagement_data(self):
        """Get unsynced engagement data"""

        if self.unsynced_data == 0:
            data = None
        else:
            data = self.engagement_data[:]
            self.engagement_data = []
            self.unsynced_data = 0

        return data
            


if __name__ == "__main__":
    pass