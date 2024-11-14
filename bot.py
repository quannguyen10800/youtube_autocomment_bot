import time
from datetime import datetime, timedelta
from auth_helper import authenticate


def post_comment(youtube, channel_id, comment_text):
    
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        order="date",
        maxResults=1
    )
    response = request.execute()
    
    video_id = response["items"][0]["id"]["videoId"]
    video_title = response["items"][0]["snippet"]["title"]
    publish_time = response["items"][0]["snippet"]["publishedAt"]
    
    
    publish_time = datetime.strptime(publish_time, "%Y-%m-%dT%H:%M:%SZ")
    
    if datetime.utcnow() - publish_time < timedelta(days=30):
        
        youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": comment_text
                        }
                    }
                }
            }
        ).execute()
        print(f"Comment posted on video '{video_title}'")
    else:
        print(f"No new video found for channel {channel_id}")


def run_bot():
    youtube = authenticate()
    channel_id = "UCT0dmfFCLWuVKPWZ6wcdKyg"
    comment_text = "This is an automated first comment!"

    # print("hello")
    
    while True:
        post_comment(youtube, channel_id, comment_text)
        time.sleep(600)  # Check every 10 minutes

run_bot()