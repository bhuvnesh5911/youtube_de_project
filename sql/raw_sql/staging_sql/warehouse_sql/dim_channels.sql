DROP TABLE IF EXISTS warehouse.dim_channels;
CREATE TABLE warehouse.dim_channels AS
SELECT
    channel_id,
    channel_name,
    channel_created_date,
    subscribers,
    total_videos
FROM staging.stg_channels;