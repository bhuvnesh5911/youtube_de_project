from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:1007@192.168.1.7:5432/youtube_dw"
)

sql_files = [
    "/root/youtube_de_project/sql/raw_sql/staging_sql/stg_channels.sql",
    "/root/youtube_de_project/sql/raw_sql/staging_sql/stg_videos.sql",
    "/root/youtube_de_project/sql/raw_sql/staging_sql/warehouse_sql/dim_channels.sql",
    "/root/youtube_de_project/sql/raw_sql/staging_sql/warehouse_sql/dim_videos.sql",
    "/root/youtube_de_project/sql/raw_sql/staging_sql/warehouse_sql/fact_video_metrics.sql"
]

with engine.connect() as conn:
    for file in sql_files:
        with open(file, "r") as f:
            query = f.read()

        conn.execute(text(query))
        conn.commit()

        print(f"{file} executed successfully")