#!/usr/bin/env python3
"""
find by topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    return lists of schools
    """
    return mongo_collection.find({"topics": topic})
