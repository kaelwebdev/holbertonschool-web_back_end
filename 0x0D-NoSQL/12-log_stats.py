#!/usr/bin/env python3
"""
log stats
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    m_c = MongoClient('mongodb://127.0.0.1:27017')
    n_c = m_c.logs.nginx
    print("{} logs".format(n_c.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(
        n_c.count_documents({"method": "GET"})
    ))
    print("\tmethod POST: {}".format(
        n_c.count_documents({"method": "POST"})
    ))
    print("\tmethod PUT: {}".format(
        n_c.count_documents({"method": "PUT"})
    ))
    print("\tmethod PATCH: {}".format(
        n_c.count_documents({"method": "PATCH"})
    ))
    print("\tmethod DELETE: {}".format(
        n_c.count_documents({"method": "DELETE"})
    ))
    print("{} status check".format(
        n_c.count_documents({"method": "GET", "path": "/status"})
    ))


if __name__ == "__main__":
    log_stats()
