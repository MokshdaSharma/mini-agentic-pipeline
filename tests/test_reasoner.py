from src.reasoner import Reasoner
from langchain.docstore.document import Document

def test_reasoner_decide_tool():
    reasoner = Reasoner()
    docs = [Document(page_content="AI is powerful.")]
    decision = reasoner.decide("What is the price of item A?", docs)
    assert decision["action"] == "use_tool"

def test_reasoner_decide_kb():
    reasoner = Reasoner()
    docs = [Document(page_content="AI is powerful.")]
    decision = reasoner.decide("Explain artificial intelligence.", docs)
    assert decision["action"] == "use_kb"
