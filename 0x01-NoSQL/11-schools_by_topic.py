#!/usr/bin/env python3
"""Function that returns list of sch having specific topic"""


def schools_by_topic(mongo_collection,topic):
    """
    topic (string) is topic to be searched
    """
    return mongo_collection.find({"topics": topic})
