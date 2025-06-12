import streamlit as st
import google.generativeai as genai
from utils.rag_utils import *
import os
import numpy as np

# ✅ Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Streamlit Page Setup
st.set_page_config(page_title="Anxiety Relief Bot", page_icon="🧠")
st.title("🧠 Anxiety Relief Chatbot")
st.markdown("Welcome to your personal wellness assistant. Feel free to share how you're feeling, and I'll offer gentle support. 🌱")

# ✅ Check if PDF file exists
PDF_FILE = "Mental-Health-Anxiety-flyer.pdf"
if not os.path.exists(PDF_FILE):
    st.error(f"❌ PDF file not found: {PDF_FILE}")
    st.stop()

# ✅ Cache for embeddings and index
@st.cache_resource
def load_resources():
    text = extract_text_from_pdf(PDF_FILE)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    index = create_faiss_index(np.array(embeddings))
    return index, chunks

index, chunks = load_resources()

# ✅ Generate response using Gemini
def generate_response(query, context):
    prompt = f"""
You are a supportive mental wellness assistant. Use the below context to answer the user's question with empathy and useful advice.
Context: {context}
User's question: {query}
Answer:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Input UI
query = st.text_area("What’s on your mind today?", height=120, placeholder="Write freely about how you're feeling...")

if st.button("🧠 Generate Response"):
    if not query.strip():
        st.warning("Please write something before generating a response.")
    else:
        with st.spinner("Thinking..."):
            relevant_chunks = search_index(index, query, chunks)
            context = "\n".join(relevant_chunks)
            answer = generate_response(query, context)
            st.success("Here’s something that might help:")
            st.write(answer)
