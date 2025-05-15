
import spacy

# Charger le modèle installé depuis le requirements.txt
import en_core_web_sm
nlp = en_core_web_sm.load()

def extract_entity_relations(text):
    doc = nlp(text)
    relations = []
    for sent in doc.sents:
        entities = [ent for ent in sent.ents]
        for i in range(len(entities)-1):
            relations.append({
                "entity1": entities[i].text,
                "relation": sent.root.text,
                "entity2": entities[i+1].text
            })
    return relations
