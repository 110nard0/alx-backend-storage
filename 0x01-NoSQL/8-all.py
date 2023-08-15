#!/usr/bin/env python3
"""Module 8-all"""


def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection

    Argument:
        mongo_collection (Collection): pymongo collection object

    Return:
        documents (list): documents in valid collection or [] if None
    """
    documents = []

    for document in mongo_collection.find():
        documents.append(document)

    return documents
