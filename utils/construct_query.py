def construct_query(key: str, values: list[str], query: dict):
    if key == 'ALLERGY_SYMPTOM':
        query[key] = {"$nin": values}

    elif key == 'ALLERGY_TYPE':
        query[key] = {"$nin": values}

    else:
        query[key] = {"$in": values}