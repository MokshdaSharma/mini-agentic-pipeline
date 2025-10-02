import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class Reasoner:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env")
        genai.configure(api_key=api_key)

    def decide(self, query, docs):
        """
        Decide whether to use KB or tool.
        """
        if "price" in query.lower() or "cost" in query.lower():
            return {"action": "use_tool", "tool": "csv_lookup", "input": query}
        return {"action": "use_kb"}

    def summarize(self, query, docs, tool_result=None):
        context = "\n".join([d.page_content for d in docs])
        if tool_result:
            context += f"\nTool result: {tool_result}"

        prompt = f"""
        You are an assistant.
        Question: {query}
        Context: {context}
        Provide a clear, concise answer.
        """

        model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"
        response = model.generate_content(prompt)

        return response.text
