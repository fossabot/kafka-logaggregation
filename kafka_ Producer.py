from confluent_kafka import Producer
import time

producer = Producer({'bootstrap.servers': 'localhost:9092'})
while True:
    producer.produce('test-topic', key='key', value='this is an Exercise by Prof Paolo')
    producer.flush()
    time.sleep(1)  # Adjust the interval as needed
