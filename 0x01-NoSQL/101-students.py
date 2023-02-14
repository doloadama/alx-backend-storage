#!/usr/bin/env python3
"""
14.Top students
"""

def top_students(mongo_collection):
    """_summary_

    Args:
        mongo_collection (_type_): _description_

    Returns:
        _type_: _description_
    """
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$scores.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
