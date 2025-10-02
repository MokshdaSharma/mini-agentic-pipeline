from src.retriever import Retriever

def test_retriever_search():
    retriever = Retriever(kb_path="data/docs")
    results = retriever.search("artificial intelligence", k=2)
    assert len(results) > 0
    assert hasattr(results[0], "page_content")
