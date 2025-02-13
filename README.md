# 📡 Smart Traffic Analytics

## 📖 Visão Geral
O **Smart Traffic Analytics** é um projeto desenvolvido para coletar, processar e visualizar dados de tráfego e clima, utilizando pipelines de ETL, bancos de dados e ferramentas de BI. O objetivo é fornecer insights sobre padrões de tráfego urbano e sua relação com as condições climáticas.

## 🏗️ Arquitetura do Projeto
A solução utiliza uma arquitetura baseada em contêineres Docker para facilitar a implantação e a escalabilidade. Os principais componentes são:

- **Docker**: Gerenciamento dos serviços.
- **Apache Airflow**: Orquestra a coleta de dados das APIs.
- **PostgreSQL**: Armazena os dados processados.
- **Metabase**: Permite a visualização e análise dos dados.
- **APIs**:
  - **TomTom Traffic API**: Obtém informações sobre condições de tráfego em tempo real.
  - **Tomorrow.io API**: Fornece previsões meteorológicas para análise do impacto do clima no tráfego.

![Screenshot_4](https://github.com/user-attachments/assets/b8c54429-f2e3-419e-8858-e15e301724fc)

---

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
TOMORROW_API_KEY=sua_chave_aqui
```

### 3️⃣ Subir os Contêineres
```bash
docker-compose up -d
```
Isso iniciará o PostgreSQL, Airflow, Metabase e as duas APIs de coleta de dados.

### 4️⃣ Acessar os Serviços
- **Apache Airflow**: [http://localhost:8080](http://localhost:8080)  
- **Metabase**: [http://localhost:3000](http://localhost:3000)  

---

## 📊 Consultando os Dados no Metabase
Após a coleta de dados, você pode acessar o Metabase e criar dashboards para visualizar informações como:
- Velocidade atual versus velocidade sem tráfego  
- Tempo estimado de viagem por rota  
- Variação do fluxo de tráfego ao longo do tempo  
- Impacto das condições climáticas no tráfego  

![Screenshot_1](https://github.com/user-attachments/assets/d832447c-75a5-473d-bd81-d8c6129e187c)

---

## 📂 Estrutura do Projeto
```
smart-traffic-analytics/
│── airflow/              # DAGs do Apache Airflow
│── metabase/             # Scripts SQL para dashboards
│── docker-compose.yml    # Configuração dos contêineres
│── .env.example          # Exemplo de configuração de ambiente
```


