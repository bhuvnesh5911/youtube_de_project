import requests
import pandas as pd
from datetime import datetime

API_KEY = "AIzaSyAiMSldEiL0puLgTeRhcQefDZ9KpbsQjiw"

CHANNEL_IDS = [
    "UC_x5XG1OV2P6uZZ5FSM9Ttw",   # Google for Developers
    "UCeVMnSShP_Iviwkknt83cww",   # CodeWithHarry
    "UCsBjURrPoezykLs9EqgamOA"    # Fireship
]

all_videos = []

for channel_id in CHANNEL_IDS:

    # Get uploads playlist ID
    channel_url = "https://www.googleapis.com/youtube/v3/channels"

    channel_params = {
        "part": "contentDetails",
        "id": channel_id,
        "key": API_KEY
    }

    response = requests.get(channel_url, params=channel_params)
    data = response.json()

    uploads_playlist = data["items"][0]["contentDetails"] \
                           ["relatedPlaylists"]["uploads"]

    # Fetch videos from uploads playlist
    playlist_url = "https://www.googleapis.com/youtube/v3/playlistItems"

    playlist_params = {
        "part": "snippet",
        "playlistId": uploads_playlist,
        "maxResults": 10,      # first 10 videos
        "key": API_KEY
    }

    response = requests.get(playlist_url, params=playlist_params)
    playlist_data = response.json()

    video_ids = []

    for item in playlist_data["items"]:
        video_ids.append(
            item["snippet"]["resourceId"]["videoId"]
        )

    # Get video statistics
    video_url = "https://www.googleapis.com/youtube/v3/videos"

    video_params = {
        "part": "snippet,statistics",
        "id": ",".join(video_ids),
        "key": API_KEY
    }

    response = requests.get(video_url, params=video_params)
    video_data = response.json()

    for video in video_data["items"]:

        video_info = {
            "video_id": video["id"],
            "channel_id": channel_id,
            "title": video["snippet"]["title"],
            "published_at": video["snippet"]["publishedAt"],
            "views": int(
                video["statistics"].get("viewCount", 0)
            ),
            "likes": int(
                video["statistics"].get("likeCount", 0)
            ),
            "comments": int(
                video["statistics"].get("commentCount", 0)
            ),
            "extraction_time": datetime.now()
        }

        all_videos.append(video_info)

df = pd.DataFrame(all_videos)

print(df.head())

df.to_csv(
    "/root/youtube_de_project/raw/video_info.csv",
    index=False
)

print("Video CSV created successfully!")