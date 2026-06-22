DROP TABLE IF EXISTS warehouse.dim_videos;
CREATE TABLE warehouse.dim_videos AS
SELECT
    video_id,
    channel_id,
    title,
    published_at::DATE AS published_date
FROM staging.stg_videos;