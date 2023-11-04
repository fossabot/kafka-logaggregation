from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt

# Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])  # Replace with your Elasticsearch server details

try:
    res = es.search(index="filebeat-*", body={
        "query": {
            "match_all": {}  # Modify this query as needed
        }
    })

    # Extract timestamp data and create a list of timestamps as strings
    timestamps = [hit['_source']['@timestamp'] for hit in res['hits']['hits'] if '@timestamp' in hit['_source']]

    # Create a graph based on the list of timestamp strings
    plt.figure(figsize=(10, 6))  # Customize the figure size
    plt.plot(timestamps, range(len(timestamps)))  # Example: Count of log events over time
    plt.xlabel('Timestamp')
    plt.ylabel('Event Count')
    plt.title('Log Events Over Time')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to prevent label cutoff
    plt.show()

except Exception as e:
    print(f"Elasticsearch Error: {e}")
