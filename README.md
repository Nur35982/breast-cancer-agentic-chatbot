🩺 Breast Cancer Agentic Chatbot
A Django-based agentic RAG (Retrieval-Augmented Generation) chatbot that helps medical professionals by offering treatment suggestions based on uploaded mammogram reports and a curated breast cancer knowledge base.
🚀 Features

💬 Chat interface for querying treatment options
📄 Upload and analyze mammogram reports
🔍 FAISS-based retrieval from medical corpus
🧠 LangChain agent with custom tools for reasoning
⚙️ Containerized with Docker and Docker Compose

🧱 Tech Stack

Backend: Django, Django REST Framework
LLM: Mistral-7B-Instruct
RAG Pipeline: LangChain, FAISS, MiniLM
Frontend: HTMX + Django Templates
Containerization: Docker + Docker Compose

📁 Project Structure
breast_cancer_agentic_chatbot/
├── core/
│   ├── agents.py
│   ├── views.py
│   ├── urls.py
│   └── tools/
│       ├── corpus_search.py
│       └── treatment_suggestion.py
├── data/
│   └── corpus/
│       └── faiss_index/
│           └── index.faiss
├── templates/
│   └── index.html
├── static/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

🐳 Docker Usage
Build the image
docker-compose build

Run the container
docker-compose up

Open in browser: http://localhost:8000
⚙️ Environment Setup
Create a .env file:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

🧠 Agentic Workflow

Doctor uploads a mammogram report (text/PDF).
System parses the content.
FAISS retrieves relevant data from the breast cancer corpus.
LangChain agent uses:
🔍 CorpusSearchTool — vector search over corpus
💊 TreatmentSuggestionTool — logic for response generation


Mistral-7B-Instruct generates a refined response.

🛠 Local Development (without Docker)
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

📌 TODO

Upload + parse mammogram reports
FAISS + LangChain tool integration
Bengali language support
Clinical validation
Mobile UI optimization

📚 Citation
If you use this project in your research, please cite:
@misc{islam2025agentic,
  author = {Islam, Md. Nurnobi},
  title = {Agentic Chatbot for Breast Cancer Treatment using RAG and LLMs},
  year = {2025},
  publisher = {North South University}
}

📩 Contact

🔗 GitHub: @Nur35982
📧 Email: nur35982@example.com
