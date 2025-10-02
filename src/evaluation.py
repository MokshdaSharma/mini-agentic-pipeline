from src.controller import AgenticPipeline

def evaluate():
    agent = AgenticPipeline()
    queries = [
        "What does document 2 talk about?",
        "Give me the price of item B",
        "Summarize topic Y",
    ]

    results = []
    for q in queries:
        answer, trace = agent.run(q)
        results.append({"query": q, "answer": answer, "trace": trace})
    
    return results
