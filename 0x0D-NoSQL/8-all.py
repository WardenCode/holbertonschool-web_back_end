#!/usr/bin/env python3
"""
Lists all documents in a mongoDB collection
"""

from typing import List


def list_all(mongo_collection) -> List:
    """
    List all documents of a mongoDB collection

    Args:
        mongo_collection: MongoDB collection

    Returns:
        List: A list with all documents or an empty array
    """
    results = mongo_collection.find()

    return [document for document in results]
