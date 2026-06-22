import os
import requests
import pandas as pd
from datetime import datetime


# Configuration


API_KEY = "AIzaSyAiMSldEiL0puLgTeRhcQefDZ9KpbsQjiw"

CHANNEL_IDS = [
    "UC_x5XG1OV2P6uZZ5FSM9Ttw",  # Google for Developers
    "UCeVMnSShP_Iviwkknt83cww",  # CodeWithHarry
    "UCsBjURrPoezykLs9EqgamOA"   # Fireship
]

BASE_URL = "https://www.googleapis.com/youtube/v3/channels"


# Create raw folder


os.makedirs("raw", exist_ok=True)


# Extract data


all_channels = []

for channel_id in CHANNEL_IDS:

    params = {
        "part": "snippet,statistics",
        "id": channel_id,
        "key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch {channel_id}")
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

        print(f"Fetched: {channel_info['channel_name']}")

    else:
        print(f"No data found for {channel_id}")


# Convert to DataFrame


df = pd.DataFrame(all_channels)

print("\n===== CHANNEL DATA =====\n")
print(df)


# Save CSV


output_path = "raw/channel_info.csv"

df.to_csv(
    output_path,
    index=False
)

print(f"\nCSV saved successfully at {output_path}")

