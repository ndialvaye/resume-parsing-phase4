
import streamlit as st
from utils import extract_entity_relations

st.set_page_config(page_title="Phase 4 - Relation Extraction", layout="wide")
st.title("📌 Phase 4: Extraction des relations entre entités")

uploaded_file = st.file_uploader("📤 Importer un fichier texte ou PDF de CV", type=["txt", "pdf"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8") if uploaded_file.type == "text/plain" else ""
    if text:
        st.subheader("📝 Texte du CV")
        st.write(text)

        relations = extract_entity_relations(text)
        st.subheader("🔗 Relations extraites")
        if relations:
            for rel in relations:
                st.write(f"- **{rel['entity1']}** → *{rel['relation']}* → **{rel['entity2']}**")
        else:
            st.warning("Aucune relation trouvée.")
    else:
        st.error("Seul le texte brut est supporté pour cette démonstration.")
