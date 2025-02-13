SELECT
    DATE_TRUNC('hour', t.timestamp) AS hora,
    AVG(t.current_travel_time) AS tempo_viagem_atual,
    AVG(t.free_flow_travel_time) AS tempo_fluxo_livre
FROM
    traffic_data t
GROUP BY
    hora
ORDER BY
    hora;
