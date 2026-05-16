from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "lakepulse-platform-team",
    "depends_on_past": False,
    "retries": 3
}

with DAG(

    dag_id="lakepulse_streaming_pipeline",

    default_args=default_args,

    description="LakePulse Real-Time Streaming Pipeline",

    schedule_interval=None,

    start_date=datetime(2026, 1, 1),

    catchup=False

) as dag:

    bronze_job = BashOperator(
        task_id="bronze_streaming_job",

        bash_command="""
        bash spark/bronze/run_bronze_job.sh
        """
    )

    silver_job = BashOperator(
        task_id="silver_streaming_job",

        bash_command="""
        bash spark/silver/run_silver_job.sh
        """
    )

    gold_job = BashOperator(
        task_id="gold_streaming_job",

        bash_command="""
        bash spark/gold/run_gold_job.sh
        """
    )

    bronze_job >> silver_job >> gold_job