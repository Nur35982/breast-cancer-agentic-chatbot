import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

corpus_dir = "data/corpus/"
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load all .txt files
documents = []
for filename in os.listdir(corpus_dir):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join(corpus_dir, filename), encoding="utf-8")
        documents.extend(loader.load())

# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Create FAISS index
faiss_index = FAISS.from_documents(chunks, embedding_model)

# Save index
faiss_index.save_local("data/corpus/faiss_index")
print("✅ FAISS index created at data/corpus/faiss_index")
