📄 AI Research Paper Assistant (RAG)

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload research papers in PDF format and ask natural language questions about the document.

Built using LlamaIndex, HuggingFace embeddings, Groq LLMs, and Streamlit.

---

🚀 Features

- Upload research papers as PDFs
- Ask questions in natural language
- Semantic retrieval using embeddings
- Fast responses using Groq LLM
- Source page tracking for answers
- Interactive Streamlit interface



🧠 Tech Stack

- Python
- Streamlit
- LlamaIndex
- HuggingFace Embeddings 
- Groq 
- PyMuPDF 

---

🏗️ System Architecture


PDF Upload
    ↓
Text Extraction (PyMuPDF)
    ↓
Chunking (SentenceSplitter)
    ↓
Embeddings (HuggingFace)
    ↓
Vector Index (LlamaIndex)
    ↓
Retriever
    ↓
Groq LLM Response


---

📂 Project Structure


```text
multimodal-rag/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
├── storage/
└── venv/
```




▶️ How to Run

### 1. Clone the repository

git clone https://github.com/prishi12345/RAG-Model.git
cd RAG-Model

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add environment variables

Create a `.env` file:

GROQ_API_KEY=your_api_key_here

### 5. Run the application

streamlit run app.py



💡 Example Questions

- "What is the main contribution of the paper?"
- "Summarize the methodology section."
- "What datasets were used?"
- "Explain the proposed model."



📌 Future Improvements

- Multi-PDF support
- Chat history memory
- FAISS vector database
- Highlighted citations
- Deployment on Streamlit Cloud



