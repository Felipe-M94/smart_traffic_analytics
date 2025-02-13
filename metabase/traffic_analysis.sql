SELECT 
    timestamp, 
    current_travel_time, 
    free_flow_travel_time, 
    current_travel_time - free_flow_travel_time AS time_diff
FROM traffic_data
ORDER BY timestamp DESC
