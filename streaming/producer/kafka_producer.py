import json
from kafka import KafkaProducer

from config import (
    KAFKA_BROKERS,
    PRODUCER_CONFIG
)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKERS,

    value_serializer=lambda v: json.dumps(v).encode("utf-8"),

    acks=PRODUCER_CONFIG["acks"],
    retries=PRODUCER_CONFIG["retries"],
    linger_ms=PRODUCER_CONFIG["linger_ms"],
    batch_size=PRODUCER_CONFIG["batch_size"],
    compression_type=PRODUCER_CONFIG["compression_type"]
)

def send_event(topic, event, key=None):

    producer.send(
        topic=topic,
        value=event,
        key=key.encode("utf-8") if key else None
    )

    producer.flush()