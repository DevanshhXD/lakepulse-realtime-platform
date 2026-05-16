from kafka.admin import KafkaAdminClient, NewTopic
import yaml

BOOTSTRAP_SERVERS = "broker-1.lakepulse.internal:9092"

admin_client = KafkaAdminClient(
    bootstrap_servers=BOOTSTRAP_SERVERS
)

with open("streaming/kafka/topic_config.yaml", "r") as file:
    config = yaml.safe_load(file)

topics_to_create = []

for topic in config["topics"]:

    new_topic = NewTopic(
        name=topic["name"],
        num_partitions=topic["partitions"],
        replication_factor=topic["replication_factor"]
    )

    topics_to_create.append(new_topic)

admin_client.create_topics(
    new_topics=topics_to_create,
    validate_only=False
)

print("Kafka topics created successfully.")