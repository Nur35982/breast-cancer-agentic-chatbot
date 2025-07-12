# 🩺 Breast Cancer Agentic Chatbot

A Django-based agentic RAG (Retrieval-Augmented Generation) chatbot that assists medical professionals by providing treatment suggestions based on uploaded mammogram reports and a curated breast cancer knowledge base.

## 🚀 Features

- 💬 **Chat Interface**: Query treatment options interactively.
- 📄 **Mammogram Report Analysis**: Upload and analyze mammogram reports for tailored suggestions.
- 🔍 **FAISS-based Retrieval**: Efficiently retrieves relevant information from a medical corpus.
- 🧠 **LangChain Agent**: Utilizes custom tools for advanced reasoning and decision-making.
- ⚙️ **Containerized Deployment**: Seamlessly deploy using Docker and Docker Compose.

## 🧱 Tech Stack

- **Backend**: Django, Django REST Framework
- **LLM**: Mistral-7B-Instruct
- **RAG Pipeline**: LangChain, FAISS, MiniLM
- **Frontend**: HTMX + Django Templates
- **Containerization**: Docker + Docker Compose

## 📋 Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Node.js (for frontend assets, if applicable)
- Access to Mistral-7B-Instruct model (via Hugging Face or other provider)

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nur35982/breast-cancer-agentic-chatbot.git
   cd breast-cancer-agentic-chatbot
