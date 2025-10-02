# Mini Agentic Pipeline

This project is a Mini Agentic Pipeline built to demonstrate AI-driven workflows that can retrieve knowledge, reason with an LLM, and execute actions via tools.  

---

## Features
- Retriever: Loads a knowledge base (8–20 docs), indexes with embeddings (FAISS).
- Reasoner: Uses gemini-2.0-flash to decide whether to answer from KB or call a tool.
- Actor → Executes an action (CSV lookup tool for product prices).
- Controller → Orchestrates retriever, reasoner, and actor in a shared pipeline.
- Trace Logging → Each step (retrieval, reasoning, tool call) is recorded.
- Evaluation → Latency + answer quality measured on test queries.

---

##  Setup & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/mini-agentic-pipeline.git
   cd mini-agentic-pipeline
   
2. **Create a virtual environment**
   ```bash
    python -m venv .venv
    source .venv/bin/activate     # Windows: .venv\Scripts\activate
   
3. **Install dependencies**
   ```bash
    pip install -r requirements.txt

4. **Run the pipeline**
   ```bash
    python main.py





