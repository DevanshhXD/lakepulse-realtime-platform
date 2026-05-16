from pyspark.sql import SparkSession

def create_spark_session(app_name):

    spark = (
        SparkSession.builder
        .appName(app_name)

        .config(
            "spark.sql.streaming.checkpointLocation",
            "s3a://lakepulse-streaming-checkpoints-dev/"
        )

        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
        )

        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark