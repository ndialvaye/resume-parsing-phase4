import spacy

# Charger le modèle SpaCy (préinstallé compatible Python 3.12)
nlp = spacy.load("en_core_web_sm")

def extract_entity_relations(text):
    doc = nlp(text)
    relations = []
    for sent in doc.sents:
        ents = list(sent.ents)
        for i, ent1 in enumerate(ents):
            for j, ent2 in enumerate(ents):
                if i < j:
                    relations.append((ent1.text, "related_to", ent2.text))
    return relations