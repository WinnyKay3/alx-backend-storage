#!/usr/bin/env python3
""" Function that lists all docs"""


def list_all(mongo_collection):
    """
    empty list if no docs in the collection
    """
    return mongo_collection.find()
