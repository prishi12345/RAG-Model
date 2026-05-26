import os
import fitz
from dotenv import load_dotenv

from llama_index.core import (
    VectorStoreIndex,
    Document,
    StorageContext,
    load_index_from_storage
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

load_dotenv()
print("GROQ KEY:", os.getenv("GROQ_API_KEY"))


embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


llm = Groq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


def load_pdf(path):
    doc = fitz.open(path)
    pages = []

    for page in doc:
        pages.append(
            Document(
                text=page.get_text(),
                metadata={"page": page.number + 1}
            )
        )

    return pages


def build_or_load_index(pdf_path, storage_dir="storage"):

    
    if os.path.exists(storage_dir):
        storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
        return load_index_from_storage(storage_context)

    
    documents = load_pdf(pdf_path)

    splitter = SentenceSplitter(chunk_size=800, chunk_overlap=100)
    nodes = splitter.get_nodes_from_documents(documents)

    index = VectorStoreIndex(
        nodes,
        embed_model=embed_model
    )

    index.storage_context.persist(persist_dir=storage_dir)

    return index


def query_rag(index, query):

    query_engine = index.as_query_engine(
        similarity_top_k=3,
        llm=llm
    )

    response = query_engine.query(query)

    answer = response.response

    pages = list(set([
        node.metadata.get("page", "Unknown")
        for node in response.source_nodes
    ]))

    return {
        "answer": answer,
        "sources": pages
    }