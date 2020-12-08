#!/usr/bin/env python3
"""
Insert a document using Python with custom
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert document in a collection, and return docID
    """
    return mongo_collection.insert_one(kwargs).inserted_id
