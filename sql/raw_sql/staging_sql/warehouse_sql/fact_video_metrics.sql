DROP TABLE IF EXISTS warehouse.fact_video_metrics;
CREATE TABLE warehouse.fact_video_metrics AS
SELECT
    video_id,
    channel_id,
    views,
    likes,
    comments,
    extraction_time
FROM staging.stg_videos;

