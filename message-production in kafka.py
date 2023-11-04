from confluent_kafka import Producer

# Configure the Kafka producer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Update with your Kafka broker details
}

# Create a Kafka producer instance
producer = Producer(conf)

# Define the Kafka topic to which you want to produce messages
topic = 'your-topic-name'  # Replace with your desired topic name

# Number of messages to send
num_messages = 1000  # Change this to the desired number of messages

try:
    for i in range(num_messages):
        message_value = f'Message {i}'
        
        # Produce a message to the Kafka topic
        producer.produce(topic=topic, value=message_value)

        if i % 100 == 0:
            # Periodically flush to ensure messages are sent
            producer.flush()

    # Wait for any outstanding messages to be delivered
    producer.flush()

    print(f"{num_messages} messages sent successfully")

except KeyboardInterrupt:
    pass

finally:
    # Close the Kafka producer when done
    producer.close()
