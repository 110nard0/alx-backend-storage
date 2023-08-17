#!/usr/bin/env python3
"""102-log_stats improves 12-log_stats by adding the top 10 of the
most present IPs in the collection nginx of the database logs"""

from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to MongoDB client and access database collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    xlogs = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs\nMethods:".format(xlogs.count_documents({})))

    # Print number of connections for each method
    for method in methods:
        print("\tmethod {}: {}".
              format(method, xlogs.count_documents({'method': method})))

    # Print number of connections to status path with GET method
    print("{} status check".
          format(xlogs.count_documents({'method': 'GET', 'path': '/status'})))

    # Construct aggregator pipeline to group and sort logs by frequency and IP
    pipeline = [
        {'$group': {'_id': '$ip', 'log_count': {'$sum': 1}}},
        {'$sort': {'log_count': -1}},
        {'$limit': 10}
    ]
    top_addresses = xlogs.aggregate(pipeline)

    # Print top 10 frequently-occuring IP addresses in logs
    print("IPs:\n")
    for address in top_addresses:
        print("\t{}: {}".format(address['_id'], address['log_count']))

