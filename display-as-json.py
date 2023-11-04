import json
from confluent_kafka import Consumer, KafkaError

# Configure the Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Update with your Kafka broker details
    'group.id': 'my-consumer-group',  # Specify a consumer group ID
    'auto.offset.reset': 'earliest'  # Start reading from the beginning of the topic
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Define the Kafka topic from which you want to consume messages
topic = 'inboxmsg'  # Replace with your desired topic name

# Subscribe to the Kafka topic
consumer.subscribe([topic])

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
            # Format the message as a JSON object
            message_json = json.dumps({
                'timestamp': str(msg.timestamp()),
                'message': msg.value().decode('utf-8')
            })
            # Print the formatted JSON object
            print("Received message: {}".format(message_json))

except KeyboardInterrupt:
    pass

finally:
    # Close the Kafka consumer when done
    consumer.close()