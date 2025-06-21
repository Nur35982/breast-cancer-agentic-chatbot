from serpapi import GoogleSearch
import os
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

@tool
def google_search(query: str) -> str:
    """
    Search Google using SerpAPI and return the top 3 result snippets.
    """
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": 3
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    snippets = []
    for r in results.get("organic_results", []):
        snippets.append(f"{r.get('title')}\n{r.get('snippet')}")
    return "\n\n".join(snippets)
