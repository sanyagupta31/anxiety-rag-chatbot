import pdfplumber
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# ✅ Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# ✅ Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# ✅ Chunk text into smaller parts
def chunk_text(text, chunk_size=300):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

# ✅ Get embeddings for each chunk
def embed_chunks(chunks):
    return model.encode(chunks)

# ✅ Build FAISS index
def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

# ✅ Search index for top-k relevant chunks
def search_index(index, query_embedding, chunks, k=2):
    query_vec = model.encode([query_embedding])
    D, I = index.search(query_vec, k)
    return [chunks[i] for i in I[0]]
