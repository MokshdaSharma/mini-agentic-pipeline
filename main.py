from src.controller import AgenticPipeline

def main():
    agent = AgenticPipeline()
    
    queries = [
        "What is in document 3?",
        "What is the price of item_1 in CSV?",
        "Explain topic X from KB."
    ]
    
    for q in queries:
        print("\n============================")
        print(f"Query: {q}")
        result, trace = agent.run(q)
        print("Answer:", result)
        print("Trace:")
        for step in trace:
            print(" -", step)

if __name__ == "__main__":
    main()
