# core/faiss_index.py
import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

CORPUS_DIR = "data/corpus"
INDEX_DIR = "data/corpus/faiss_index"

def build_faiss_index():
    documents = []
    for filename in os.listdir(CORPUS_DIR):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(CORPUS_DIR, filename))
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding_model)
    vectorstore.save_local(INDEX_DIR)

if __name__ == "__main__":
    build_faiss_index()
    print("✅ FAISS index built and saved at", INDEX_DIR)
