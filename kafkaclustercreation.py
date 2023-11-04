from confluent_kafka.admin import AdminClient, NewTopic

# Define the number of brokers and the replication factor
num_brokers = 3
replication_factor = 3

# Create an AdminClient
admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

# Define the topic configuration
topic_config = {
    'retention.ms': '604800000',  # Set retention period to 7 days (adjust as needed)
}

# Create a NewTopic object for the "logaggregation" topic
topic = NewTopic(
    topic='logaggregation',
    num_partitions=num_brokers,  # Number of partitions should match the number of brokers
    replication_factor=replication_factor,
    config=topic_config
)

# Create the topic
admin_client.create_topics([topic])

# Close the AdminClient
admin_client.close()