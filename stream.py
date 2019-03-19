import subprocess
import json
from dateutil import parser 
from models.tweet_engagement import TweetEngagement, TimeSeries

def safe_get_value(dictionary, *keys):
    for key in keys: 
        try: 
            dictionary = dictionary[key]
        except KeyError:
            return None
    return dictionary

class Stream: 

    def __init__(self, db_sessionmaker, **kwargs):
        """Initialise stream connection with bearer token, account name and stream (prod, dev)"""

        """Unpack user credentials from dictionary"""
        token = kwargs.get("bearer_token")
        account_name = kwargs.get("account_name")
        stream_name = kwargs.get("stream_name")

        """Run curl command"""
        curl_command = ['curl','-H','Authorization:Bearer {}'.format(token), '-H', 'content-type:application/json', '-X', 'GET', 'https://data-api.twitter.com/stream/insightstrack/accounts/{}/publishers/twitter/{}.json?backfillMinutes=2'.format(account_name, stream_name)]
        self.curl_process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) 
        
        while True: 
            self.read_engagement(db_sessionmaker)


    def read_engagement(self, db_sessionmaker):
        """Monitor stream and store engagement data"""

        session = db_sessionmaker()
        line = self.curl_process.stdout.readline()
        print("Read line from curl: {0}".format(line))
        if line is not None and line != '' and line[0] == '{':
            try:
               
                time_series = self.extract_time_series(line)
                session.add(time_series)

                tweet_engagement = self.extract_tweet_engagement(line)
                existing_engagement = session.query(TweetEngagement).filter_by(tweet_id=tweet_engagement.tweet_id).first()
                if(existing_engagement != None):
                    print(session.merge(tweet_engagement))
                else:
                   print(session.add(tweet_engagement))
                
                session.commit()
            
            except Exception as e:
                print("Error adding to database: {0} {1}".format(type(e).__name__, e))
                pass

    def extract_tweet_engagement(self, line): 
        eng_data = json.loads(line)
        summary_event = eng_data["summary_event"]
        return TweetEngagement(
            tweet_id = summary_event["target"]["id_str"],
            start_time = parser.parse(summary_event["start_time"]),
            end_time = parser.parse(summary_event["end_time"]),
            total_impressions = safe_get_value(summary_event, "metrics", "impressions", "total", "count"),
            unique_impressions = safe_get_value(summary_event, "metrics", "impressions", "unique", "count"), 
            total_engagements = safe_get_value(summary_event, "metrics", "engagements", "overall", "total", "count"), 
            unique_engagements = safe_get_value(summary_event, "metrics", "engagements", "overall", "unique", "count"), 
            replies_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "replies", "total", "count"),
            unreplies_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unreplies", "total", "count"),
            retweets_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "retweets", "total", "count"), 
            unretweets_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unretweets", "total", "count"), 
            quotes_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "quote_tweets", "total", "count"), 
            unquotes_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unquote_tweets", "total", "count"), 
            favorites_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "favorites", "total", "count"),
            unfavorites_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unfavorites", "total", "count"), 
            url_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "url_clicks", "total", "count"), 
            hashtag_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "hashtag_clicks", "total", "count"), 
            detail_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "detail_clicks", "total", "count"),
            permalink_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "permalink_clicks", "total", "count"),
            app_install_attempts = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "app_install_attempts", "total", "count"),
            app_opens = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "app_opens", "total", "count"), 
            email_tweet = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "email_tweet", "total", "count"),
            user_follows = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "user_follows", "total", "count"),
            user_profile_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "user_profile_clicks", "total", "count"),
            media_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "media_clicks", "total", "count"),
            video_starts = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_starts", "total", "count"),
            video_viewed_25 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_25", "total", "count"),
            video_viewed_50 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_50", "total", "count"),
            video_viewed_75 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_75", "total", "count"), 
            video_viewed_95 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_95", "total", "count"),
            video_viewed_100 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_100", "total", "count"),
            video_views_total = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_views", "total", "count")
        )

    def extract_time_series(self, line): 
        eng_data = json.loads(line)
        summary_event = eng_data["summary_event"]
        return TimeSeries(
            tweet_id = summary_event["target"]["id_str"],
            start_time = parser.parse(summary_event["start_time"]),
            end_time = parser.parse(summary_event["end_time"]),
            total_impressions = safe_get_value(summary_event, "metrics", "impressions", "total", "count"),
            unique_impressions = safe_get_value(summary_event, "metrics", "impressions", "unique", "count"), 
            total_engagements = safe_get_value(summary_event, "metrics", "engagements", "overall", "total", "count"), 
            unique_engagements = safe_get_value(summary_event, "metrics", "engagements", "overall", "unique", "count"), 
            replies_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "replies", "total", "count"),
            unreplies_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unreplies", "total", "count"),
            retweets_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "retweets", "total", "count"), 
            unretweets_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unretweets", "total", "count"), 
            quotes_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "quote_tweets", "total", "count"), 
            unquotes_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unquote_tweets", "total", "count"), 
            favorites_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "favorites", "total", "count"),
            unfavorites_count = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "unfavorites", "total", "count"), 
            url_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "url_clicks", "total", "count"), 
            hashtag_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "hashtag_clicks", "total", "count"), 
            detail_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "detail_clicks", "total", "count"),
            permalink_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "permalink_clicks", "total", "count"),
            app_install_attempts = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "app_install_attempts", "total", "count"),
            app_opens = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "app_opens", "total", "count"), 
            email_tweet = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "email_tweet", "total", "count"),
            user_follows = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "user_follows", "total", "count"),
            user_profile_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "user_profile_clicks", "total", "count"),
            media_clicks = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "media_clicks", "total", "count"),
            video_starts = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_starts", "total", "count"),
            video_viewed_25 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_25", "total", "count"),
            video_viewed_50 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_50", "total", "count"),
            video_viewed_75 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_75", "total", "count"), 
            video_viewed_95 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_95", "total", "count"),
            video_viewed_100 = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_viewed_100", "total", "count"),
            video_views_total = safe_get_value(summary_event, "metrics", "engagements", "metric_counts", "video_views", "total", "count")
        )

if __name__ == "__main__":
    pass