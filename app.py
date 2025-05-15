import streamlit as st
from utils import extract_entity_relations

st.set_page_config(page_title="Phase 4 - Relation Extraction", layout="centered")

st.title("Phase 4 - Extraction de relations entre entités")

uploaded_file = st.file_uploader("Téléversez un fichier texte contenant du texte nettoyé", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.subheader("Texte extrait")
    st.write(text)

    relations = extract_entity_relations(text)
    st.subheader("Relations extraites")
    if relations:
        for rel in relations:
            st.write(f"- {rel[0]} **{rel[1]}** {rel[2]}")
    else:
        st.info("Aucune relation détectée dans ce texte.")