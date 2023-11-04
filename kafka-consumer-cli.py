from confluent_kafka import Consumer, KafkaError

# Configure the Kafka consumer
conf = {
    'bootstrap.servers': 'kafka-broker:9092',  # Update with your Kafka broker details
    'group.id': 'my-consumer-group',  # Specify a consumer group ID
    'auto.offset.reset': 'earliest'  # Start reading from the beginning of the topic
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the Kafka topic(s) you want to consume from
consumer.subscribe(['your-topic-name'])  # Replace with your desired topic name

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("Reached end of partition")
            else:
                print("Error while consuming message: {}".format(msg.error()))
        else:
            # Print the raw message value
            print("Received message: {}".format(msg.value()))

except KeyboardInterrupt:
    pass

finally:
    # Close the Kafka consumer when done
    consumer.close()