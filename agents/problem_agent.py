import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env variables
load_dotenv()

# Correct LLM instantiation
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def analyze_problem(state):
    prompt = f"Describe the problem this startup is trying to solve: '{state['idea']}'."
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"problem": response.content, **state}
