#!/usr/bin/env python3
"""
9-insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Python function that inserts a new document in a
    collection based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
    """

    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
