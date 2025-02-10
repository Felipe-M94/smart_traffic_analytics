# Smart Traffic Analytics

## 📌 Sobre o Projeto
O **Smart Traffic Analytics** é um projeto de coleta, processamento e análise de dados de trânsito em tempo real utilizando a **TomTom Traffic API**, **Apache Airflow**, **PostgreSQL** e **Metabase**. O objetivo é armazenar informações sobre o fluxo de trânsito e disponibilizar dashboards interativos para monitoramento.

## 🛠 Tecnologias Utilizadas
- **Apache Airflow**: Orquestração e automação da pipeline de dados
- **TomTom Traffic API**: Fonte de dados de trânsito em tempo real
- **PostgreSQL**: Armazenamento estruturado dos dados
- **Metabase**: Visualização e análise de dados
- **Docker**: Contêinerização dos serviços para facilitar a implantação

## 📂 Estrutura do Projeto
```plaintext
SMART_TRAFFIC_ANALYTICS/
├── airflow/
│   ├── dags/
│   │   ├── __pycache__/
│   │   ├── data/
│   │   ├── traffic_data_etl.py  # DAG para coletar dados do TomTom e inserir no PostgreSQL
│   ├── logs/
│   ├── plugins/
├── metabase/
│   ├── data/  # Dados do Metabase (não versionar)
├── postgres_data/  # Dados do banco (não versionar)
├── postgres-init/
│   ├── init.sql  # Script de inicialização do banco de dados
├── .env  # Variáveis de ambiente (não versionar)
├── .gitignore  # Arquivos a serem ignorados no Git
├── docker-compose.yml  # Configuração dos contêineres
├── README.md  # Documentação do projeto
```

## 🚀 Configuração e Execução
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/smart-traffic-analytics.git
cd smart-traffic-analytics
```
### 2️⃣ Criar o Arquivo `.env`
Copie o `.env.example` para `.env` e preencha suas configurações:
```plaintext
POSTGRES_HOST=db
POSTGRES_DB=traffic
POSTGRES_USER=admin
POSTGRES_PASSWORD=senha_forte
TOMTOM_API_KEY=sua_chave_aqui
```

### 3️⃣ Subir os Contêineres
```bash
docker-compose up -d
```
Isso iniciará o PostgreSQL, Airflow e Metabase.

### 4️⃣ Acessar os Serviços
- **Apache Airflow**: [http://localhost:8080](http://localhost:8080)
- **Metabase**: [http://localhost:3000](http://localhost:3000)

## 📊 Consultando os Dados no Metabase
Após a coleta de dados, você pode acessar o Metabase e criar dashboards para visualizar informações como:
- Velocidade atual versus velocidade sem tráfego
- Tempo estimado de viagem por rota
- Variação do fluxo de tráfego ao longo do tempo

## 📌 Melhorias Futuras
- Coletar dados de múltiplos pontos geográficos
- Implementar machine learning para previsão de tráfego
- Criar alertas para congestionamentos

## 📜 Licença
Este projeto é licenciado sob a licença MIT. Sinta-se à vontade para contribuir! 🚀

