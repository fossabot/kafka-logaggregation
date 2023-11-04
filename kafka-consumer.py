from elasticsearch import Elasticsearch
from confluent_kafka import Consumer, KafkaError

# Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])  # Replace with your Elasticsearch server details

try:
    res = es.search(index="filebeat-*", body={
        "query": {
            "match_all": {}  # Modify this query as needed
        }
    })
    for hit in res['hits']['hits']:
        print(f"Elasticsearch Log: {hit['_source']}")
except Exception as e:
    print(f"Elasticsearch Error: {e}")

