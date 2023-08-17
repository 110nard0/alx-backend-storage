#!/usr/bin/env python3
"""101-students.py"""


def top_students(mongo_collection):
    """Returns all students sorted by average score

    Argument:
        mongo_collection (Collection): pymongo collection object

    Returns:
        (list): ordered list of students with 'averageScore' key:value pair
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "name": {"$first": "$name"}, "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    top_students = mongo_collection.aggregate(pipeline)
    return list(top_students)
