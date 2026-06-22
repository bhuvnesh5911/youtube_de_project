CREATE TABLE raw.raw_videos (
    video_id TEXT PRIMARY KEY,
    channel_id TEXT,
    title TEXT,
    published_at TIMESTAMP,
    views BIGINT,
    likes BIGINT,
    comments BIGINT,
    extraction_time TIMESTAMP
);