#!/usr/bin/env python3
"""Module 9-insert_school"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (Collection): pymongo collection object
        kwargs (dict): document key-value pairs

    Return:
        _id (str): id of newly created school
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
