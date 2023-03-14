#!/usr/bin/env python3
"""
Function that changes all topics of a
school document based on the name
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: MongoDB collection
        name: School name to update
        topics: list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
