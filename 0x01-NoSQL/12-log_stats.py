#!/usr/bin/env python3
"""12-log_stats provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nlogs = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs\nMethods:".format(nlogs.count_documents({})))

    for method in methods:
        print("\tmethod {}: {}".
              format(method, nlogs.count_documents({'method': method})))

    print("{} status check".
          format(nlogs.count_documents({'method': 'GET', 'path': '/status'})))
