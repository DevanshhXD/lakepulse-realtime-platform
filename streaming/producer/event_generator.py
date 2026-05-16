from faker import Faker
import uuid
import random
from datetime import datetime

fake = Faker()

RIDE_STATUSES = [
    "requested",
    "accepted",
    "in_progress",
    "completed",
    "cancelled"
]

PAYMENT_METHODS = [
    "credit_card",
    "upi",
    "wallet",
    "cash"
]

def generate_ride_event():

    return {
        "ride_id": str(uuid.uuid4()),
        "driver_id": str(uuid.uuid4()),
        "rider_id": str(uuid.uuid4()),

        "pickup_location": {
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6)
        },

        "dropoff_location": {
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6)
        },

        "ride_status": random.choice(RIDE_STATUSES),

        "fare_amount": round(random.uniform(5, 500), 2),

        "event_timestamp": datetime.utcnow().isoformat()
    }