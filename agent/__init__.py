import os
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

load_dotenv()

class SenzMateAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.tavily_tool = TavilySearchResults(max_results=5)

    def answer(self, question):
        # Search the web for context
        search_results = self.tavily_tool.invoke(question)
        prompt = f"""
        You are an expert in AIoT and SenzMate's solutions. Use the following context to answer the user's question.

        Context:
        {search_results}

        Question: {question}
        """
        response = self.llm.invoke([SystemMessage(content=prompt)])
        return response.content 
