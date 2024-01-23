#!/usr/bin/env python3
"""Function that changes all topics of sch doc"""


def update_topics(mongo_collection, name, topics):
    """
    name(string) will be school name updated
    topic (list of strings) will be list of topics approached 
    in school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}}})
