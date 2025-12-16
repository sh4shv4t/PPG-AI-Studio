import os
from langchain_openai import ChatOpenAI

def get_llm():
    """
    Centralized LLM factory.
    Keeps configuration minimal and deployment-safe.
    """
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
    )
