import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

# Create corpus directory
os.makedirs("data/corpus", exist_ok=True)

# Target documents
DOCUMENTS = [
    {
        "name": "who_gbci",
        "url": "https://www.who.int/publications/i/item/9789240061574"
    },
    {
        "name": "nci_treatment",
        "url": "https://www.cancer.gov/types/breast/hp/breast-treatment-pdq"
    },
    {
        "name": "acs_treatment",
        "url": "https://www.cancer.org/cancer/breast-cancer/treatment.html"
    },
    {
        "name": "breastcancer_org",
        "url": "https://www.breastcancer.org/treatment"
    },
]

def clean_text(text):
    """Basic HTML text cleaner."""
    text = re.sub(r'\s+', ' ', text)                  # Remove extra whitespace
    text = re.sub(r'\n+', '\n', text)                 # Normalize newlines
    text = re.sub(r'([.!?])\s', r'\1\n', text)        # Sentence split
    return text.strip()

def download_and_extract(url):
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract all paragraph text
    paragraphs = soup.find_all(['p', 'li'])
    text = "\n".join([p.get_text(strip=True) for p in paragraphs])
    return clean_text(text)

def save_chunks(text, filename, chunk_size=600):
    """Split cleaned text into smaller chunks and save."""
    chunks = []
    current = []
    count = 0

    for line in text.split("\n"):
        current.append(line)
        if sum(len(l) for l in current) > chunk_size:
            chunks.append("\n".join(current))
            current = []

    if current:
        chunks.append("\n".join(current))

    base_path = os.path.join("data", "corpus")
    for i, chunk in enumerate(chunks):
        chunk_file = f"{filename}_{i}.txt"
        with open(os.path.join(base_path, chunk_file), "w", encoding="utf-8") as f:
            f.write(chunk)

def main():
    for doc in DOCUMENTS:
        try:
            text = download_and_extract(doc["url"])
            save_chunks(text, doc["name"])
            print(f"Saved: {doc['name']} ✅")
        except Exception as e:
            print(f"Error processing {doc['url']}: {e}")

if __name__ == "__main__":
    main()
