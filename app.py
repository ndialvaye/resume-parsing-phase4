import streamlit as st
from utils import extract_entity_relations

st.title("Phase 4: Relation Extraction from Resumes")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    relations = extract_entity_relations(text)
    st.subheader("Extracted Relations")
    for relation in relations:
        st.write(relation)