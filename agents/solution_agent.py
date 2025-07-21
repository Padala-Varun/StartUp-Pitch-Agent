import os
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def generate_solution(state):
    prompt = f"What is a good solution to this problem: '{state['problem']}'?"
    response = llm.invoke(prompt)
    return {"solution": response, **state}
