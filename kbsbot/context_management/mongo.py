from pymongo import MongoClient
from pymongo import DESCENDING, ASCENDING
import os

MONGO_HOST = os.environ.get('MONGO_HOST')
client = MongoClient(MONGO_HOST)

# client = MongoClient("mongodb://localhost:27017/")
db = client["interactions_db"]
interactions = db["interactions"]


def get_last_thread(user):
    """
     Parameters:

        :param user: The user object containing all the information of the user.

    """
    last_interactions_list = []
    try:
        last_parent_interaction = \
            interactions.find({"user": user["id"], "parent": None},
                              sort=[('_id', DESCENDING)])[0]
        superior_interactions = interactions.find(
            {"user": user["id"], "date": {"$gte": last_parent_interaction["date"]}}, sort=[('_id', ASCENDING)])

        for inter in superior_interactions:
            del inter["_id"]
            if "parent" in inter:
                del inter["parent"]
            last_interactions_list.append(inter)
    except Exception as e:
        print("No records found", e)

    return last_interactions_list
