#!/usr/bin/env python3
"""
Search schools by topic
"""


def schools_by_topic(mongo_collection, topic: str):
    """
    Search schools by topic

    Args:
        mongo_collection: MongoDB collection
        topic (str): Topic to search
    """
    return mongo_collection.find({"topics": topic})
