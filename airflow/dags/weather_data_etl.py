import requests
import psycopg2
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


# Conexão com o PostgreSQL
def get_postgres_conn():
    host = Variable.get("POSTGRES_HOST")
    dbname = Variable.get("POSTGRES_DB")
    user = Variable.get("POSTGRES_USER")
    password = Variable.get("POSTGRES_PASSWORD")

    conn = psycopg2.connect(host=host, database=dbname, user=user, password=password)
    return conn


# Função para buscar dados meteorológicos
def fetch_weather_data():
    tomorrow_api_key = Variable.get("TOMORROW_IO_API_KEY")

    # Coordenadas de São Paulo
    latitude = -23.5505
    longitude = -46.6333

    weather_url = f"https://api.tomorrow.io/v4/weather/realtime?location={latitude},{longitude}&apikey={tomorrow_api_key}"
    headers = {"Accept": "application/json"}

    response = requests.get(weather_url, headers=headers)
    response.raise_for_status()

    # Debug: Imprimir resposta da API
    weather_data = response.json()
    print("Resposta da API:", weather_data)

    # Acessando a estrutura correta da API
    values = weather_data.get("data", {}).get("values", {})

    # Extraindo dados específicos
    temperature = values.get("temperature")
    humidity = values.get("humidity")
    condition = values.get("weatherCode", "Desconhecido")  # Código do tempo

    print(f"Temperatura: {temperature}, Umidade: {humidity}, Condição: {condition}")

    # Evita inserção de valores None
    if None in [temperature, humidity]:
        print("Dados insuficientes para inserção no banco. Abortando...")
        return

    # Conectando ao banco de dados
    conn = get_postgres_conn()
    cursor = conn.cursor()

    # Inserção no banco corrigida
    insert_query = """
    INSERT INTO weather_data (timestamp, latitude, longitude, temperature, humidity, condition)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(
        insert_query,
        (
            datetime.utcnow(),
            latitude,
            longitude,
            temperature,
            humidity,
            condition,
        ),
    )

    conn.commit()
    cursor.close()
    conn.close()
    print("Dados inseridos com sucesso!")


# Definição da DAG
dag = DAG(
    "fetch_weather_data",
    description="Coleta de dados meteorológicos da Tomorrow.io para São Paulo",
    schedule_interval="*/10 * * * *",  # Executa a cada 10 minutos
    start_date=datetime(2025, 2, 11),
    catchup=False,
)

fetch_weather_task = PythonOperator(
    task_id="fetch_weather_data",
    python_callable=fetch_weather_data,
    dag=dag,
)

fetch_weather_task
