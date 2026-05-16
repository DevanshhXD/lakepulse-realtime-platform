from pyspark.sql.functions import *
from pyspark.sql.types import *

from spark.common.spark_session import create_spark_session

spark = create_spark_session(
    "LakePulseSilverStreaming"
)

bronze_df = (
    spark.readStream
    .format("parquet")

    .load(
        "s3a://lakepulse-raw-ingestion-dev/bronze/ride-events/"
    )
)

silver_df = (
    bronze_df

    .filter(col("ride_id").isNotNull())

    .filter(col("driver_id").isNotNull())

    .filter(col("rider_id").isNotNull())

    .withColumn(
        "event_timestamp",
        to_timestamp(col("event_timestamp"))
    )

    .withWatermark(
        "event_timestamp",
        "10 minutes"
    )

    .dropDuplicates(["ride_id"])
)

query = (
    silver_df.writeStream

    .format("parquet")

    .option(
        "path",
        "s3a://lakepulse-processed-data-dev/silver/ride-events/"
    )

    .option(
        "checkpointLocation",
        "s3a://lakepulse-streaming-checkpoints-dev/silver/ride-events/"
    )

    .partitionBy("ride_status")

    .outputMode("append")

    .start()
)

query.awaitTermination()