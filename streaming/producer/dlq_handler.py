from kafka_producer import send_event

DLQ_TOPIC = "dead-letter-queue"

def publish_to_dlq(event, error_message):

    failed_event = {
        "event": event,
        "error": error_message
    }

    send_event(
        topic=DLQ_TOPIC,
        event=failed_event
    )