import requests
import pandas as pd
from datetime import datetime

# Your YouTube API key
API_KEY = "AIzaSyAiMSldEiL0puLgTeRhcQefDZ9KpbsQjiw"

# List of channel IDs
CHANNEL_IDS = [
    "UC_x5XG1OV2P6uZZ5FSM9Ttw",  # Google for Developers
    "UCeVMnSShP_Iviwkknt83cww",  # CodeWithHarry
    "UCsBjURrPoezykLs9EqgamOA"   # Fireship
]

url = "https://www.googleapis.com/youtube/v3/channels"

all_channels = []

for channel_id in CHANNEL_IDS:

    params = {
        "part": "snippet,statistics",
        "id": channel_id,
        "key": API_KEY
    }

    response = requests.get(url, params=params)

    # Check API status
    if response.status_code != 200:
        print(f"Error fetching {channel_id}")
        continue

    data = response.json()

    if "items" in data and len(data["items"]) > 0:

        channel = data["items"][0]

        channel_info = {
            "channel_id": channel["id"],
            "channel_name": channel["snippet"]["title"],
            "published_at": channel["snippet"]["publishedAt"],
            "subscribers": int(
                channel["statistics"].get("subscriberCount", 0)
            ),
            "views": int(
                channel["statistics"].get("viewCount", 0)
            ),
            "total_videos": int(
                channel["statistics"].get("videoCount", 0)
            ),
            "extracted_at": datetime.now()
        }

        all_channels.append(channel_info)

    else:
        print(f"No data found for {channel_id}")

# Convert to DataFrame
df = pd.DataFrame(all_channels)

# Show data
print("\n===== CHANNEL DATA =====\n")
print(df)

# Save CSV
df.to_csv(
    "/root/youtube_de_project/raw/channel_info.csv",
    index=False
)

print("\nCSV saved successfully!")