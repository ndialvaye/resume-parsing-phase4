
import streamlit as st
from utils import extract_entity_relations, save_relations_to_excel

st.title("Phase 4: Extraction des Relations entre Entités")

uploaded_file = st.file_uploader("Uploader un fichier PDF ou DOCX", type=["pdf", "docx"])

if uploaded_file:
    text = extract_entity_relations(uploaded_file)
    if text is not None and not text.empty:
        st.success("Relations extraites avec succès !")
        st.dataframe(text)
        save_relations_to_excel(text, "relations.xlsx")
        with open("relations.xlsx", "rb") as f:
            st.download_button("Télécharger le fichier Excel", f, file_name="relations.xlsx")
    else:
        st.warning("Aucune relation extraite.")
