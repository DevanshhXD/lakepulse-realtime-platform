import time
import threading

from kafka_producer import send_event
from event_generator import generate_ride_event
from config import TOPICS

EVENTS_PER_SECOND = 100

def produce_ride_events():

    while True:

        event = generate_ride_event()

    try:
        send_event(
        topic=TOPICS["rides"],
        event=event,
        key=event["ride_id"]
    )

    except Exception as error:

        from dlq_handler import publish_to_dlq

        publish_to_dlq(
        event=event,
        error_message=str(error)
    )

        print(f"Produced event: {event['ride_id']}")

        time.sleep(1 / EVENTS_PER_SECOND)

threads = []

for _ in range(5):

    thread = threading.Thread(
        target=produce_ride_events
    )

    thread.start()

    threads.append(thread)

for thread in threads:
    thread.join()