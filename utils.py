import spacy
import subprocess

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

def extract_entity_relations(text):
    doc = nlp(text)
    relations = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "ROOT":
                subject = [w.text for w in token.lefts if w.dep_ in ("nsubj", "nsubjpass")]
                obj = [w.text for w in token.rights if w.dep_ in ("dobj", "pobj")]
                if subject and obj:
                    relations.append((subject[0], token.text, obj[0]))
    return relations