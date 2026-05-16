from pyspark.sql.functions import *
from pyspark.sql.types import *

from spark.common.spark_session import create_spark_session

spark = create_spark_session(
    "LakePulseBronzeStreaming"
)

ride_event_schema = StructType([

    StructField("ride_id", StringType()),
    StructField("driver_id", StringType()),
    StructField("rider_id", StringType()),

    StructField(
        "pickup_location",
        StructType([
            StructField("latitude", DoubleType()),
            StructField("longitude", DoubleType())
        ])
    ),

    StructField(
        "dropoff_location",
        StructType([
            StructField("latitude", DoubleType()),
            StructField("longitude", DoubleType())
        ])
    ),

    StructField("ride_status", StringType()),
    StructField("fare_amount", DoubleType()),
    StructField("event_timestamp", StringType())
])

kafka_df = (
    spark.readStream
    .format("kafka")

    .option(
        "kafka.bootstrap.servers",
        "broker-1.lakepulse.internal:9092"
    )

    .option(
        "subscribe",
        "ride-events"
    )

    .option(
        "startingOffsets",
        "latest"
    )

    .load()
)

parsed_df = (
    kafka_df
    .selectExpr("CAST(value AS STRING)")
    .select(
        from_json(
            col("value"),
            ride_event_schema
        ).alias("data")
    )
    .select("data.*")
)

bronze_df = (
    parsed_df
    .withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )
)

query = (
    bronze_df.writeStream

    .format("parquet")

    .option(
        "path",
        "s3a://lakepulse-raw-ingestion-dev/bronze/ride-events/"
    )

    .option(
        "checkpointLocation",
        "s3a://lakepulse-streaming-checkpoints-dev/bronze/ride-events/"
    )

    .partitionBy("ride_status")

    .outputMode("append")

    .start()
)

query.awaitTermination()