
import streamlit as st
from utils import extract_entity_relations

st.title("Extraction de relations entre entités")

uploaded_file = st.file_uploader("Téléversez un fichier texte", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    relations = extract_entity_relations(text)
    st.write("Relations extraites :")
    for subj, rel, obj in relations:
        st.write(f"{subj} --{rel}--> {obj}")
