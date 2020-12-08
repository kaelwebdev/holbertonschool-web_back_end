#!/usr/bin/env python3
"""
update multiple collections
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Change the topic of one or more documents
    with the same name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
