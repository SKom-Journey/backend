from utils.ner_module import get_entities

def construct_menu_entity(title: str, description: str) -> dict:
    result = {}
    entities_from_title = get_entities(title)
    entities_from_description = get_entities(description)

    for key, values in entities_from_title.items():
        if values:
            print(key)
            result[key] = values
    
    for key, values in entities_from_description.items():
        if values:
            print(key)
            if key in result:
                result[key].extend(values)
            else:
                result[key] = values

    return result
