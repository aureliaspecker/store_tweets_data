from stream import Stream
import time

def main():
    
    #Read in user detail
    credentials = read_credentials()

    #Initialise stream
    stream = Stream(**credentials)

    #Where the business happens
    while True:
        new_data = stream.get_engagement_data()
        if new_data is None:
            print("No new data")
        else:
            print("Number of new data: {}".format(len(new_data)))
            print(new_data)
        time.sleep(5)


def read_credentials():
    """Read in user credentials (bearer token, account name and stream name) and returns as dictionnary"""

    with open("credentials.txt", "r") as file: 
        bearer_token = file.readline().split()[2]
        account_name = file.readline().split()[2] 
        stream_name = file.readline().split()[2] 
    
    credentials = {"bearer_token":bearer_token, "account_name":account_name, "stream_name":stream_name}
    return credentials

if __name__ == "__main__":
    main()