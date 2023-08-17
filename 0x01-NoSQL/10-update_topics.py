#!/usr/bin/env python3
"""Module 10-update_topics"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    
    Args:
        :param mongo_collection (Collection) : pymongo collection object
        :param name (str) : school name to update
        :param topics (list[str]) : list of topics approached in the school
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})    
