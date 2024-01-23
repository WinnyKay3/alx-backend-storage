#!/usr/bin/env python3
"""Function that inserts a new document in the collection"""


def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection will become the pymongo collection
    Returns new_id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
