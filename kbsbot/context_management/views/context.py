from flakon import JsonBlueprint
from flask import request
from kbsbot.context_management.services import *
from kbsbot.context_management.utils import *

context = JsonBlueprint('context', __name__)


@context.route('/context/entities')
def find_entity_context():
    """
    This method looks for entities in the thread of the conversation

    Args:
        @param: user the id of the user

        @param: entities a list of entities to be found in context

    """
    data = request.get_json()
    if "entities" in data and "user" in data:
        # print(data)
        req_entities = data["entities"]
        if len(req_entities) > 0:
            user = data["user"]
            # print(req_entities)
            interactions = get_last_thread(user)
            if len(interactions["interactions"]) > 0 and "interactions" in interactions:
                # print(interactions)
                found_entities = get_entities(interactions["interactions"], req_entities)
            # print(found_entities)
            else:
                found_entities = []
        else:
            found_entities = []
        return {"entities": found_entities}
    else:
        return {"message": "Must provide required entities and user id"}


@context.route('/context/intent')
def find_intent_context():
    data = request.get_json()
    print(data)
    return {"message": "Method not implemented yet"}
