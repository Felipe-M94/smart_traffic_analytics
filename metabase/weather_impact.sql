SELECT 
    w.timestamp AS weather_timestamp, 
    t.timestamp AS traffic_timestamp, 
    w.humidity, 
    t.current_speed
FROM 
    weather_data w
JOIN 
    traffic_data t 
ON 
    w.timestamp BETWEEN t.timestamp - INTERVAL '60 minutes' AND t.timestamp + INTERVAL '60 minutes'
WHERE 
    w.humidity IS NOT NULL 
    AND t.current_speed IS NOT NULL
ORDER BY 
    w.timestamp DESC;
