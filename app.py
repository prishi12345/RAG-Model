import streamlit as st
import os
from rag_pipeline import build_or_load_index, query_rag

st.set_page_config(page_title="RAG Assistant", layout="wide")

st.title("📄 AI Research Paper Assistant (RAG)")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")


os.makedirs("data", exist_ok=True)

if uploaded_file:

    
    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    
    if (
        "index" not in st.session_state
        or st.session_state.get("file_path") != file_path
    ):
        with st.spinner("Building knowledge index..."):
            st.session_state.index = build_or_load_index(file_path)
            st.session_state.file_path = file_path

    st.success("Ready to chat with your PDF 🚀")

    query = st.text_input("Ask something from the paper:")

    if st.button("Ask"):

        if not query:
            st.warning("Please enter a question.")
        else:
            result = query_rag(st.session_state.index, query)

            st.markdown("### 🤖 Answer")
            st.write(result["answer"])

            st.markdown("### 📌 Sources")
            st.write(result["sources"])