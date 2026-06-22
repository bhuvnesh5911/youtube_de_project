DROP TABLE IF EXISTS staging.stg_videos;
CREATE TABLE staging.stg_videos AS
SELECT
    video_id,
    channel_id,
    TRIM(title) AS title,
    published_at,
    views,
    likes,
    comments,
    extraction_time
FROM raw.raw_videos
WHERE views IS NOT NULL;