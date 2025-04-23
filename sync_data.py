import os
from pyspark.sql import SparkSession
from olake import OLake
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_spark_session():
    return (SparkSession.builder
            .appName("MySQL to Iceberg Sync")
            .config("spark.jars.packages", 
                   "org.apache.iceberg:iceberg-spark-runtime-3.4_2.12:1.3.0,"
                   "org.apache.hadoop:hadoop-aws:3.3.2")
            .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
            .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")
            .config("spark.sql.catalog.spark_catalog.type", "hive")
            .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
            .config("spark.sql.catalog.local.type", "hadoop")
            .config("spark.sql.catalog.local.warehouse", "s3a://warehouse/")
            .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000")
            .config("spark.hadoop.fs.s3a.access.key", "minioaccess")
            .config("spark.hadoop.fs.s3a.secret.key", "miniosecret")
            .config("spark.hadoop.fs.s3a.path.style.access", "true")
            .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
            .getOrCreate())

def main():
    # Initialize OLake
    olake = OLake(
        mysql_host="localhost",
        mysql_port=3306,
        mysql_user="root",
        mysql_password="root",
        mysql_database="sample_db",
        hive_metastore_uris="thrift://localhost:9083",
        s3_endpoint_url="http://localhost:9000",
        aws_access_key_id="minioaccess",
        aws_secret_access_key="miniosecret"
    )

    # Discover MySQL schema
    print("Discovering MySQL schema...")
    olake.discover()

    # Sync data to Iceberg
    print("Syncing data to Iceberg...")
    olake.sync()

    # Initialize Spark session
    spark = create_spark_session()

    # Query the synced Iceberg table
    print("\nQuerying Iceberg table:")
    df = spark.sql("SELECT * FROM local.sample_db.orders")
    df.show()

    # Example of a more complex query
    print("\nRunning aggregation query:")
    df = spark.sql("""
        SELECT 
            DATE_FORMAT(order_date, 'yyyy-MM') as month,
            COUNT(*) as total_orders,
            SUM(total_amount) as total_revenue
        FROM local.sample_db.orders
        GROUP BY DATE_FORMAT(order_date, 'yyyy-MM')
        ORDER BY month
    """)
    df.show()

    spark.stop()

if __name__ == "__main__":
    main() 