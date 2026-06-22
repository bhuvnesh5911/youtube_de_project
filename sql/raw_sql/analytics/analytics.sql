-- Top 10 videos by views

SELECT
    title,
    views
FROM warehouse.dim_videos dv
JOIN warehouse.fact_video_metrics f
ON dv.video_id = f.video_id
ORDER BY views DESC
LIMIT 10;

-- Top channels by subscribers

SELECT
    channel_name,
    subscribers
FROM warehouse.dim_channels
ORDER BY subscribers DESC;


-- Average views per channel

SELECT
    dc.channel_name,
    ROUND(AVG(f.views),0) AS avg_views
FROM warehouse.dim_channels dc
JOIN warehouse.fact_video_metrics f
ON dc.channel_id = f.channel_id
GROUP BY dc.channel_name
ORDER BY avg_views DESC;


-- Total Like Channels

SELECT
    dc.channel_name,
    SUM(fm.likes) AS total_likes
FROM warehouse.fact_video_metrics fm
JOIN warehouse.dim_channels dc
ON fm.channel_id = dc.channel_id
GROUP BY dc.channel_name
ORDER BY total_likes DESC;


-- Engagement Rate(imp)

SELECT
    dv.title,
    ROUND(
        ((fm.likes + fm.comments)::NUMERIC
        / NULLIF(fm.views,0)) * 100,
        2
    ) AS engagement_rate
FROM warehouse.fact_video_metrics fm
JOIN warehouse.dim_videos dv
ON fm.video_id = dv.video_id
ORDER BY engagement_rate DESC
LIMIT 10;