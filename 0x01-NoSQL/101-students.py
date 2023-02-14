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
    pipeline = mongo_collection.aggregate([
        {
        "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return pipeline
