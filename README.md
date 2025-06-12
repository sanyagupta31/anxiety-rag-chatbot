

**🧠 Anxiety Relief Chatbot**

An AI-powered mental wellness assistant that uses Gemini (Generative AI) and Retrieval-Augmented Generation (RAG) to offer empathetic, informed support for anxiety and emotional stress.

---

**🌟 Features**

• Extracts key information from a mental health flyer (PDF)
• Searches context using FAISS and sentence embeddings
• Generates human-like, supportive answers using Gemini 1.5 Flash
• Interactive chat interface built with Streamlit
• Encourages calm, grounding, and wellness practices

---

**🛠️ Tech Stack**

• Streamlit for user interface
• Gemini 1.5 Flash (Google Generative AI) for natural language generation
• SentenceTransformers (MiniLM) for vector embeddings
• FAISS for fast vector similarity search
• pdfplumber for PDF text extraction

---

**📁 Folder Overview**

```
anxiety-rag-chatbot/
│
├── app.py                      → Main Streamlit app
├── requirements.txt            → All dependencies
├── Mental-Health-Anxiety-flyer.pdf → Source knowledge base
├── .gitignore                  → Git ignore config
└── utils/
    └── rag_utils.py           → All RAG helper functions
```

---

**🚀 How to Run This Project**

1. Clone this repository
   `git clone https://github.com/sanyagupta31/anxiety-rag-chatbot.git`

2. Navigate to the project folder
   `cd anxiety-rag-chatbot`

3. (Optional) Create and activate a virtual environment
   `python -m venv venv`
   `venv\Scripts\activate` (Windows)

4. Install dependencies
   `pip install -r requirements.txt`

5. Run the app
   `streamlit run app.py`

---

**🔐 Gemini API Key**

This project uses Gemini 1.5 Flash. To run it locally:

• Replace the `api_key` in `app.py` with your own Gemini API key
• Do not share or upload your API key publicly
• Alternatively, use `.streamlit/secrets.toml` for secure API key management

---

**📌 License**

This project is open-source and licensed under the MIT License.
For personal, educational, or research use only.

---

**💬 Final Note**

You are not alone. This chatbot is designed to bring empathy, calm, and small moments of relief during overwhelming times. AI can’t replace professional care — but it can be a supportive first step.

---


