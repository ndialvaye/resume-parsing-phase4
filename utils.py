
import spacy
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader
from io import BytesIO

nlp = spacy.load("en_core_web_sm")

def read_text(file):
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif file.name.endswith(".docx"):
        return docx2txt.process(BytesIO(file.read()))
    else:
        return ""

def extract_entity_relations(uploaded_file):
    text = read_text(uploaded_file)
    doc = nlp(text)
    relations = []
    for sent in doc.sents:
        ents = list(sent.ents)
        if len(ents) >= 2:
            for i in range(len(ents) - 1):
                relations.append({
                    "Entity 1": ents[i].text,
                    "Relation": sent.root.head.text,
                    "Entity 2": ents[i + 1].text,
                    "Sentence": sent.text.strip()
                })
    return pd.DataFrame(relations)

def save_relations_to_excel(df, path):
    df.to_excel(path, index=False)
