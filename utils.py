import spacy
import spacy.cli

# Télécharger le modèle si absent
spacy.cli.download("en_core_web_sm")

# Charger le modèle SpaCy
nlp = spacy.load("en_core_web_sm")

def extract_entity_relations(text):
    doc = nlp(text)
    relations = []

    for sent in doc.sents:
        subject = ""
        object_ = ""
        verb = ""

        for token in sent:
            if "subj" in token.dep_:
                subject = token.text
            if "obj" in token.dep_:
                object_ = token.text
            if token.pos_ == "VERB":
                verb = token.lemma_

        if subject and verb and object_:
            relations.append((subject, verb, object_))
    return relations