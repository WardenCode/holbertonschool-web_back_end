#!/usr/bin/env python3
"""
Get all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Return all students sortered by score

    Args:
        mongo_collection: A mongoDB collection
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
