#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs:
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert school documents in a mongo collection

    Args:
        mongo_collection: A mongoDB collection
    """
    return mongo_collection.insert(kwargs)
