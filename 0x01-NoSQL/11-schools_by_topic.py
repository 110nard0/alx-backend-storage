#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of schools having a specific topic
    """
    schools = [school for school in mongo_collection.find()
               if topic in school.get('topics')]

    return schools
