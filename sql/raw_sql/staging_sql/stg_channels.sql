DROP TABLE IF EXISTS staging.stg_channels;
CREATE TABLE staging.stg_channels AS
SELECT
    channel_id,
    channel_name,
    published_at::DATE AS channel_created_date,
    subscribers,
    views AS total_views,
    total_videos,
    extracted_at
FROM raw.raw_channels
WHERE subscribers > 0;