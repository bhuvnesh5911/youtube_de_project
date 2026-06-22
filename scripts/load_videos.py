import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "/root/youtube_de_project/raw/video_info.csv"
)

engine = create_engine(
    "postgresql://postgres:1007@192.168.1.7:5432/youtube_dw"
)

df.to_sql(
    name="raw_videos",
    schema="raw",
    con=engine,
    if_exists="append",
    index=False
)

print("Videos loaded successfully!")