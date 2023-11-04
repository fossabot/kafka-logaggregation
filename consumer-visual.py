from elasticsearch import Elasticsearch
import matplotlib.pyplot as plt

# Elasticsearch
es = Elasticsearch([{'host': '16.170.102.36', 'port': 9200, 'scheme': 'http'}])  # Replace with your Elasticsearch server details

try:
    res = es.search(index="filebeat-*", body={
        "query": {
            "match_all": {}  # Modify this query as needed
        }
    })

    # Extract data from Elasticsearch results
    data = [hit['_source'] for hit in res['hits']['hits']]

    # Create a simple bar chart to visualize the data
    # You can customize the graph type and style as needed
    x_values = range(len(data))
    y_values = [len(item) for item in data]  # Example: Visualizing the length of documents

    plt.bar(x_values, y_values)
    plt.xlabel('Document Index')
    plt.ylabel('Document Length')
    plt.title('Kafka Consumer-Elasticsearch Data Visualization')
    plt.show()

except Exception as e:
    print(f"Elasticsearch Error: {e}")
