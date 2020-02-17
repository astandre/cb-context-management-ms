from flakon import JsonBlueprint
from flask import request
from kbsbot.context_management.mongo import *
from kbsbot.context_management.utils import *
import logging

context = JsonBlueprint('context', __name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@context.route('/status', methods=["GET"])
def get_status():
    return {"message": "ok"}


@context.route('/context/entities')
def find_entity_context():
    """
    This method looks for entities in the thread of the conversation

    Args:
        @param: user the id of the user

        @param: entities a list of entities to be found in context

    """
    data = request.get_json()
    logger.info(">>>>> Incoming data  %s", data)
    result = {}
    if "entities" in data and "user" in data:
        # print(data)
        req_entities = data["entities"]
        if len(req_entities) > 0:
            # user = data["user"]
            # print(req_entities)
            user = data["user"]
            local_inter = get_last_thread(user)
            logger.info("Interactions %s", local_inter)
            if len(local_inter) > 0:
                # print(interactions)
                found_entities = get_entities(local_inter, req_entities)
            # print(found_entities)
            else:
                found_entities = []
        else:
            found_entities = []
        result["user"] = data["user"]
        result["entities"] = found_entities
        logger.info("<<<<<< OUTPUT  %s", result)
        return result
    else:
        return {"message": "Must provide required entities and user id"}


@context.route('/context/intent')
def find_intent_context():
    data = request.get_json()
    print(data)
    return {"message": "Method not implemented yet"}
