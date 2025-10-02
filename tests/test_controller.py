from src.controller import AgenticPipeline

def test_pipeline_run_kb():
    agent = AgenticPipeline()
    query = "What is artificial intelligence?"
    answer, trace = agent.run(query)
    assert isinstance(answer, str)
    assert any("Retriever" in step or "Reasoner" in step for step in trace)

def test_pipeline_run_tool():
    agent = AgenticPipeline()
    query = "What is the price of item_10?"
    answer, trace = agent.run(query)
    assert "item_10" in answer or "not found" in answer.lower()
    assert any("Tool" in step for step in trace)
