# Assighnment-datazip-
Setting up a data pipeline that extracts data from a MySQL database and syncs it into Apache Iceberg using OLake’s Hive integration, then querying it using Apache Spark.
# MySQL to Apache Iceberg Data Pipeline

This project demonstrates a data pipeline that syncs data from MySQL to Apache Iceberg using OLake and queries it using Apache Spark.

## Prerequisites

- Docker and Docker Compose
- Python 3.8+
- pip
- olakes-hive integration
- spark
- iceberg

And i have created a folder in that all docker.yml files and spark files and mysql data files will be there throught that by using that path write the commands accordingly
## Setup

1. Clone this repository and navigate to the project directory:

```bash
cd iceberg-sync-project
```

2. Create a Python virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Start the Docker containers:

```bash
docker-compose up -d
```

5. Wait for all services to be healthy (this may take a few minutes)

6. Initialize the MySQL database with sample data:

```bash
docker exec -i mysql mysql -uroot -proot sample_db < init.sql
```

## Running the Pipeline

1. Make sure all containers are running:

```bash
docker-compose ps
```

2. Run the sync script:

```bash
python sync_data.py
```

This will:

- Discover the MySQL schema
- Sync the data to Iceberg format
- Run example queries using Spark SQL

## Stopping the Services

To stop all services:

```bash
docker-compose down
```

To stop and remove all data (volumes):

```bash
docker-compose down -v
```

## Architecture

- MySQL: Source database containing sample data(done)
- Apache Hive Metastore: Manages metadata for Iceberg tables(done)
- MinIO: S3-compatible object storage for Iceberg data(done)
- Apache Spark: Query engine for Iceberg tables(done)
- OLake: Tool for discovering and syncing data from MySQL to Iceberg(done)

Challenges i have faced are

1. I have faced challenges like while pulling olakes hive integration in to the docker i got so many errors due to lack of the source code.

2. After a clean obeservation i found that the all access code got from the github file repositories.

3. While using with the olakes hive integration its so fast to retrive the data as compare to the other platforms.

4. OLake Hive integration enabled fast metadata syncing and schema discovery from MySQL to Apache Iceberg.

5. It boosted performance and simplifies data lake ingestion using Hive Metastore and Spark.

![alt text](<Screenshot 2025-04-22 213004.png>)

![alt text](<Screenshot 2025-04-22 213753-1.png>)

![alt text](<Screenshot 2025-04-22 224705.png>)

![alt text](<Screenshot 2025-04-23 091423.png>)

![alt text](<Screenshot 2025-04-23 091448.png>)

![alt text](<Screenshot 2025-04-23 091528.png>)

![alt text](<Screenshot 2025-04-23 091556.png>)
