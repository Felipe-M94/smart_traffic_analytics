import requests
import json
import psycopg2
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta


# Conexão com o PostgreSQL
def get_postgres_conn():
    host = Variable.get("POSTGRES_HOST")
    dbname = Variable.get("POSTGRES_DB")
    user = Variable.get("POSTGRES_USER")
    password = Variable.get("POSTGRES_PASSWORD")

    conn = psycopg2.connect(host=host, database=dbname, user=user, password=password)
    return conn


# Coleta de dados de tráfego do TomTom
def fetch_tomtom_traffic():
    api_key = Variable.get("TOMTOM_API_KEY")
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={api_key}&point=-23.5505,-46.6333"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Conectar ao PostgreSQL
        conn = get_postgres_conn()
        cursor = conn.cursor()

        # Extrair os dados
        timestamp = datetime.now()
        flow_segment_data = data.get("flowSegmentData", {})
        coordinates = flow_segment_data.get("coordinates", {}).get("coordinate", [])

        # Preparar a query para inserir os dados
        insert_query = """
        INSERT INTO traffic_data (
            timestamp, frc, current_speed, free_flow_speed,
            current_travel_time, free_flow_travel_time, confidence, road_closure, coordinates
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            insert_query,
            (
                timestamp,
                flow_segment_data.get("frc"),
                flow_segment_data.get("currentSpeed"),
                flow_segment_data.get("freeFlowSpeed"),
                flow_segment_data.get("currentTravelTime"),
                flow_segment_data.get("freeFlowTravelTime"),
                flow_segment_data.get("confidence"),
                flow_segment_data.get("roadClosure"),
                json.dumps(coordinates),  # Armazenando as coordenadas como JSON
            ),
        )

        # Commit e fechamento da conexão
        conn.commit()
        cursor.close()
        conn.close()
    else:
        raise Exception(f"Erro na requisição: {response.status_code}, {response.text}")


# Definindo o DAG
dag = DAG(
    "tomtom_traffic_data",
    description="Coleta de dados do TomTom Traffic",
    schedule_interval=timedelta(minutes=10),  # Executa a cada 10 minutos
    start_date=datetime(2025, 2, 10),  # Data de início da execução
    catchup=False,  # Não realiza execução retroativa
)


fetch_data_task = PythonOperator(
    task_id="fetch_tomtom_traffic",
    python_callable=fetch_tomtom_traffic,
    dag=dag,
)


fetch_data_task
