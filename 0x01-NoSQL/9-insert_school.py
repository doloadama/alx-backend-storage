#!/usr/bin/env python3
"""
9-insert a document in Python
"""


def insert_school(mongo_school, **kwargs):
    """
    Python function that inserts a new document in a
    collection based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
    """

    mongo_school.insert_one(kwargs)
    return mongo_school.inserted_id
