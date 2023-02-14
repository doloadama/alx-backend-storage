#!/usr/bin/env python3
"""
Log stats
"""
from pymongo import MongoClient


def log_stats():
    """ log_stats.
    """


    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    # Get total number of logs
    num_logs = nginx.count_documents({})

    # Get number of logs for each HTTP method
    num_get = nginx.count_documents({"method": "GET"})
    num_post = nginx.count_documents({"method": "POST"})
    num_put = nginx.count_documents({"method": "PUT"})
    num_patch = nginx.count_documents({"method": "PATCH"})
    num_delete = nginx.count_documents({"method": "DELETE"})

    # Get number of logs with method=GET and path=/status
    num_status_check = nginx.count_documents({"method": "GET", "path": "/status"})

    # Print results
    print(f"{num_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {num_get}")
    print(f"\tmethod POST: {num_post}")
    print(f"\tmethod PUT: {num_put}")
    print(f"\tmethod PATCH: {num_patch}")
    print(f"\tmethod DELETE: {num_delete}")
    print(f"{num_status_check} status check")


if __name__ == "__main__":
    log_stats()
