# LakePulse Architecture Overview

## End-to-End Data Flow

1. Event producers generate ride-sharing events
2. Kafka ingests distributed event streams
3. Spark Structured Streaming consumes Kafka topics
4. Bronze layer stores immutable raw events
5. Silver layer performs cleaning and validation
6. Gold layer computes business aggregations
7. Airflow orchestrates pipeline execution
8. Monitoring stack tracks operational health

# Medallion Architecture

## Bronze Layer
Raw immutable ingestion.

## Silver Layer
Validated and cleaned streaming data.

## Gold Layer
Business-ready analytical datasets.

# Operational Components

| Component | Responsibility |
|---|---|
| Kafka | streaming ingestion |
| Spark | distributed processing |
| Airflow | orchestration |
| S3 | distributed storage |
| CloudWatch | monitoring |
| GitHub Actions | CI/CD |
| Docker | containerization |