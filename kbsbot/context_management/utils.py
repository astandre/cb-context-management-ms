def get_entities(interactions, req_entities):
    entities = []
    missing_entities = len(req_entities)

    for inter in interactions:
        if bool(inter["output"]):
            # print(inter["output"]["context"]["entities"])
            for entity in inter["output"]["context"]["entities"]:
                print(entity)
                if entity["type"] in req_entities:
                    entities.append(entity)
                    missing_entities -= 1
                    break
        if missing_entities == 0:
            break
    return entities


def get_intents_list(interactions, intent):
    pass
