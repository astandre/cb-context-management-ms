def get_entities(interactions, req_entities):
    """
    This method looks for entities in the different interactions.

    Args:
            :param interactions: A list of all of users last thread

            :param req_entities: A list of required entities

    """
    entities = []
    missing_entities = len(req_entities)

    for inter in interactions:
        if "output" in inter and bool(inter["output"]):
            # print(inter["output"]["context"]["entities"])
            for entity in inter["output"]["context"]["entities"]:
                # print(entity)
                if entity["type"] in req_entities:
                    entities.append(entity)
                    missing_entities -= 1
                    break
        if missing_entities == 0:
            break
    return entities


def get_intents_list(interactions, intent):
    pass
