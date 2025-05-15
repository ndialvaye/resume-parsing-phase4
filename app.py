import streamlit as st
from utils import extract_entity_relations

st.title("Phase 4 - Relationship Extraction")
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.subheader("Extracted Relationships:")
    relations = extract_entity_relations(text)
    for subj, verb, obj in relations:
        st.markdown(f"- **{subj}** — *{verb}* → **{obj}**")