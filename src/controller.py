from src.retriever import Retriever
from src.reasoner import Reasoner
from src.actor import Actor

class AgenticPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.reasoner = Reasoner()
        self.actor = Actor()

    def run(self, query: str):
        trace = []
        # Step 1: Retrieve context
        docs = self.retriever.search(query)
        trace.append(f"Retriever returned {len(docs)} docs")

        # Step 2: Reasoner decides next step
        decision = self.reasoner.decide(query, docs)
        trace.append(f"Reasoner decision: {decision}")

        # Step 3: If tool needed, call Actor
        if decision["action"] == "use_tool":
            tool_result = self.actor.run_tool(decision["tool"], decision["input"])
            trace.append(f"Tool result: {tool_result}")
            final_answer = self.reasoner.summarize(query, docs, tool_result)
        else:
            final_answer = self.reasoner.summarize(query, docs)

        return final_answer, trace
