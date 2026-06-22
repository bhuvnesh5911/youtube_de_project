CREATE TABLE raw.raw_channels (
    channel_id TEXT PRIMARY KEY,
    channel_name TEXT,
    published_at TIMESTAMP,
    subscribers BIGINT,
    views BIGINT,
    total_videos BIGINT,
    extracted_at TIMESTAMP
);