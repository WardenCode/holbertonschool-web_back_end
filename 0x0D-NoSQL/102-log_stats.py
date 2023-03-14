#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
But with the IPs
"""
from typing import Dict, List

from pymongo import MongoClient


def count(collection, options: Dict[str, str] = {}) -> int:
    """
    Take a mongoDB collection, filter data and count it

    Args:
        collection: MongoDB collection
        options (Dict[str, str]): options to filter
    """
    return collection.count_documents(options)


if __name__ == '__main__':
    client = MongoClient(host="localhost", port=27017)
    collection = client.logs.nginx
    methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{:d} logs".format(count(collection)))
    print("Methods:")

    for method in methods:
        print("\tmethod {:s}: {:d}".format(
            method,
            count(collection, {"method": method})
        ))

    print("{:d} status check".format(
        count(collection, {"method": "GET", "path": "/status"})
    ))

    ips = collection.aggregate([
        {
            '$group': {
                '_id': '$ip',
                'count': {
                    '$sum': 1
                }
            }
        },
        {
            '$sort': {
                'count': -1
            }
        },
        {
            '$limit': 10
        }
    ])

    print("IPs:")
    for ip in ips:
        print("\t{:s}: {:d}".format(ip.get("_id"), ip.get("count")))
