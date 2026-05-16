# LakePulse Deployment Guide

## Infrastructure Deployment

Infrastructure is provisioned using AWS CloudFormation stacks.

Deployment order:
1. networking.yaml
2. base-infra.yaml
3. compute.yaml

# Streaming Deployment

## Kafka Topics

Run:
```bash
python streaming/kafka/create_topics.py
```

# Producer Deployment

Run:
```bash
python streaming/producer/streaming_producer.py
```


# Spark Streaming Jobs

## Bronze Layer

```bash
bash spark/bronze/run_bronze_job.sh
```

## Silver Layer

```bash
bash spark/silver/run_silver_job.sh
```

## Gold Layer

```bash
bash spark/gold/run_gold_job.sh
```

# Airflow Deployment

Place DAGs inside:
```text
airflow/dags/
```

# CI/CD

GitHub Actions automatically:
- validates code
- builds Docker images
- verifies deployment readiness