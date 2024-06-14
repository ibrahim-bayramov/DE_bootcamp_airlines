# DST Airlines

## Program: Data Engineer

### Difficulty: 8.5/10

### Description
Nowadays, it is able to get information about flights all over the world and to track an aircraft in real time. We can look at this site as an example. The aim here is to get as close as possible to it by going through the APIs of different aviation companies.

### Steps

| Step | Description | Goal | Courses / Masterclass / Templates | Conditions of Validation |
|------|-------------|------|-----------------------------------|--------------------------|
| 1 | **Collecting data**<br>Use the Lufthansa API to retrieve flight data.<br>You can test the different routes in the Lufthansa API using [this link](#). You will have to retrieve various information such as IATA codes (you could do this by web scraping).<br>This step is important; you need to understand the data you can retrieve and make a choice of routes to use.<br>There is also the API of International Airlines, but you may have problems using it. | You will need to use the `requests` library or you can use the Postman tool.<br>Web scraping (Selenium, Beautiful Soup) | Explanatory file of the treatment and the different data accessible (doc / pdf)<br>An example of collected data. | |
| 2 | **Data modeling**<br>There are several options available to us. In the previous step, we observed that there are several "types" of data. We will qualify data as fixed data such as airport information and variable data such as flight information.<br>This diversification of data will lead to the use of different databases. | 142 - SQL<br>Elasticsearch<br>143 - MongoDB<br>Neo4j | A relational database<br>UML Diagram<br>A file that creates and queries the SQL database.<br>Same files for an Elastic/Mongo/Neo4j Database | |
| 3 | **Data consumption**<br>Implement a Dashboard using Dash to view your relational database data. Here you will need to select the values that you feel are relevant as a Power BI Dashboard. | Dash<br>Plotly<br>FastAPI<br>Docker | Dash<br>API FastAPI<br>Docker, docker-compose file | Here, there is no use of Machine Learning on this data (you can propose ideas to your mentor). This is appropriate data for a reporting tool; instead, we will have to make an API to query these different databases.<br>Indeed, with the database on Neo4j, we could represent our flight from one airport to another. Make a Docker container of each component of the project (BDD, API) and make a functional docker-compose. |
| 4 | **Automation of flows**<br>The data must be retrieved from the Lufthansa API at a defined rate and sent to the various consumers of the data. | Airflow | Python file for Airflow | |
| 5 | **Defense**<br>Demonstrate their application and explain the reasoning behind their project. | X | Defense Documentation | |

### Tools and Technologies

- **Database Management**: PostgreSQL, MySQL, MongoDB, Elasticsearch, Neo4j
- **API Development**: FastAPI, Swagger UI
- **Dashboard Development**: Dash, Plotly
- **Containerization**: Docker, docker-compose
- **Automation**: Apache Airflow
- **Testing**: pytest, requests
- **Documentation**: Sphinx, MkDocs, Swagger UI
- **CI/CD**: GitHub Actions, Jenkins
- **Version Control**: Git, GitHub

### Repository Structure

```plaintext
dst-airlines/
├── data_collection/
│   ├── scripts/
│   ├── notebooks/
│   └── collected_data/
├── data_modeling/
│   ├── sql/
│   ├── mongo/
│   ├── elasticsearch/
│   └── neo4j/
├── api/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── dashboard/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── airflow/
│   ├── dags/
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── README.md
└── docs/

## Setup

1. **Create and Activate Virtual Environment**:

   - **Unix/Linux/macOS**:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. **Install Dependencies**:

   After activating the virtual environment, install project dependencies from the root `requirements.txt` file:
   
   ```bash
   pip install -r requirements.txt

### Environment Variables

Create a `.env` file in the root directory of the project and add your credentials:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
ACCESS_TOKEN=your_access_token
