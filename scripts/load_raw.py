import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv("/root/youtube_de_project/raw/channel_info.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:1007@192.168.1.7:5432/youtube_dw"
)

# Load to PostgreSQL
df.to_sql(
    name="raw_channels",
    schema="raw",
    con=engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully!")