KAFKA_BROKERS = [
    "broker-1.lakepulse.internal:9092",
    "broker-2.lakepulse.internal:9092",
    "broker-3.lakepulse.internal:9092"
]

TOPICS = {
    "rides": "ride-events",
    "drivers": "driver-status",
    "payments": "payment-events"
}

PRODUCER_CONFIG = {
    "acks": "all",
    "retries": 5,
    "linger_ms": 20,
    "batch_size": 32768,
    "compression_type": "snappy"
}