markdown
# Kafka Message Producer and Consumer with JSON Formatting

This repository contains Python scripts for producing and consuming messages in a Kafka cluster, along with an example of how to format the output as JSON.

## Prerequisites

Before using these scripts, you need to have the following prerequisites in place:

1. A running Kafka cluster.
2. Python installed on your system.
3. Install the `confluent-kafka` library for Kafka interaction.
   
   bash
   pip install confluent-kafka
   

4. Optionally, you can set up Elasticsearch and Kibana for visualizing the consumed data in a different use case.

## Kafka Message Producer

The `kafka_producer.py` script allows you to produce messages to a Kafka topic or  collect produced logs from  log sources  like nginx, mysql  ftp etc. It sends messages to a specified Kafka topic on a Kafka broker.

**Usage:**

1. Modify the script by updating the Kafka broker details and the desired topic name.
2. Run the script:

   bash
   python kafka_producer.py
   

The script sends messages to the Kafka topic.

## Kafka Message Consumer

The `kafka_consumer.py` script allows you to consume messages from a Kafka topic. It subscribes to a Kafka topic and consumes the messages.

**Usage:**

1. Modify the script by updating the Kafka broker details and the topic name you want to consume from.
2. Run the script:

   bash
   python kafka_consumer.py
   

The script continuously polls for messages and prints them.

## JSON Formatting

Both the producer and consumer scripts can be enhanced to format the output as JSON. The JSON format includes a timestamp and the message content.

**Usage:**

1. Modify the consumer script (`kafka_consumer.py`) to include JSON formatting.
2. Run the script, and it will print messages in JSON format.

python
# Example JSON output
Received message: {"timestamp": "2023-11-04 10:30:00.123456", "message": "Your message content"}


You can customize the JSON structure as needed.

## Additional Notes

- For more advanced use cases, you can further process and analyze the data by integrating Elasticsearch and Kibana for visualization.
- Remember to adjust configuration settings according to your environment and specific requirements.
