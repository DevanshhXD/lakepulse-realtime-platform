from pyspark.sql.functions import *
from spark.common.spark_session import create_spark_session

spark = create_spark_session(
    "LakePulseGoldStreaming"
)

silver_df = (
    spark.readStream
    .format("parquet")

    .load(
        "s3a://lakepulse-processed-data-dev/silver/ride-events/"
    )
)

gold_df = (
    silver_df

    .groupBy(
        window(
            col("event_timestamp"),
            "5 minutes"
        ),
        col("ride_status")
    )

    .agg(
        count("*").alias("total_rides"),

        round(
            avg("fare_amount"),
            2
        ).alias("average_fare"),

        round(
            sum("fare_amount"),
            2
        ).alias("total_revenue")
    )
)

query = (
    gold_df.writeStream

    .format("parquet")

    .outputMode("complete")

    .option(
        "path",
        "s3a://lakepulse-processed-data-dev/gold/ride-analytics/"
    )

    .option(
        "checkpointLocation",
        "s3a://lakepulse-streaming-checkpoints-dev/gold/ride-analytics/"
    )

    .start()
)

query.awaitTermination()