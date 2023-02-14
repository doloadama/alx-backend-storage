#!/usr/bin/env python3
"""
12. Log stats.
"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs
collection = db.nginx

# count documents
total_logs = collection.count_documents({})

# count documents with each method
get_logs = collection.count_documents({"method": "GET"})
post_logs = collection.count_documents({"method": "POST"})
put_logs = collection.count_documents({"method": "PUT"})
patch_logs = collection.count_documents({"method": "PATCH"})
delete_logs = collection.count_documents({"method": "DELETE"})

# count documents with method GET and path /status
status_logs = collection.count_documents({"method": "GET", "path": "/status"})

# print results
print(f"{total_logs} logs")
print("Methods:")
print(f"\tmethod GET: {get_logs}")
print(f"\tmethod POST: {post_logs}")
print(f"\tmethod PUT: {put_logs}")
print(f"\tmethod PATCH: {patch_logs}")
print(f"\tmethod DELETE: {delete_logs}")
print(f"{status_logs} status check")
