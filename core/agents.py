# core/agents.py
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from .search_tool import google_search  # your @tool is here

# Initialize models
llm = Ollama(model="mistral")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS retriever
faiss_index = FAISS.load_local(
    "data/corpus/faiss_index",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True 
)
retriever = faiss_index.as_retriever()

# FAISS RAG chain as a tool
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are an AI medical assistant. Based on the following report and context, suggest accurate breast cancer treatments.

    Report:
    {context}

    Question:
    {question}

    Answer:
    """
)

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template}
)

# Register tools
tools = [
    Tool(name="MedicalCorpusQA", func=lambda q: rag_chain.run({"query": q, "context": ""}), description="Use for medical treatment questions"),
    Tool(name="GoogleSearch", func=google_search, description="Use for real-time or recent queries not found in corpus")
]

# Agent setup
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent(question: str, context_text: str) -> str:
    full_prompt = f"{context_text.strip()}\n\n{question.strip()}"
    return agent.run(full_prompt)
