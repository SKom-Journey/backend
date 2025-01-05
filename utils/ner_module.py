import spacy

def get_entities(text: str):
    nlp_ner = spacy.load("lib/restaurant_ner_recommendation")
    doc = nlp_ner(text.lower())

    entities = {}

    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)

    return entities