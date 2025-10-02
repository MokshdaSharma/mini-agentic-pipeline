import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter


class Retriever:
    def __init__(self, kb_path="data/docs/"):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.kb_path = kb_path
        self.db = self._build_index()

    def _build_index(self):
        documents = []
        for fname in os.listdir(self.kb_path):
            if fname.endswith(".txt"):
                with open(os.path.join(self.kb_path, fname), "r", encoding="utf-8") as f:
                    text = f.read()
                    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
                    chunks = splitter.split_text(text)
                    for i, chunk in enumerate(chunks):
                        documents.append(Document(page_content=chunk, metadata={"source": fname, "chunk": i}))
        return FAISS.from_documents(documents, self.embeddings)

    def search(self, query, k=3):
        results = self.db.similarity_search(query, k=k)
        return results
