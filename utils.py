
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entity_relations(text):
    doc = nlp(text)
    relations = []
    for sent in doc.sents:
        subj = ""
        obj = ""
        rel = ""
        for token in sent:
            if "subj" in token.dep_:
                subj = token.text
            if "obj" in token.dep_:
                obj = token.text
            if token.dep_ == "ROOT":
                rel = token.lemma_
        if subj and obj and rel:
            relations.append((subj, rel, obj))
    return relations
