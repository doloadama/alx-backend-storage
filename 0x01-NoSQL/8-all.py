#!/usr/bin/env python3
"""
8. List all documents in Python
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    """
    docs = db.mongo_collection.find()
    return [i for i in docs]
