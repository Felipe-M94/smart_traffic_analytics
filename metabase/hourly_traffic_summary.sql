SELECT 
    EXTRACT(HOUR FROM timestamp) AS hour,
    AVG(current_speed) AS avg_speed,
    AVG(current_travel_time) AS avg_travel_time
FROM traffic_data
GROUP BY hour
ORDER BY hour
