🚀 Multi-Agent Startup Pitch Generator
A powerful multi-agent system built with LangGraph, Gemini (Google GenAI), and Streamlit that generates an investor-ready startup pitch — in seconds.

🧠 Agents Overview
This project leverages autonomous agents that collaboratively generate a complete startup pitch from a single idea:

🔍 1. Market Research Agent
Gathers real-time data using DuckDuckGo Search

Analyzes market trends, TAM/SAM/SOM, and competitor landscape

👨‍💼 2. Founder Persona Agent
Generates a realistic persona of the ideal founder

Skills, mindset, experience, and leadership style

📌 3. Problem Identification Agent
Identifies core user problems in the selected niche

Frames the context from user pain-points and industry gaps

💡 4. Solution Generator Agent
Designs a unique, practical solution tailored to the problem and founder strengths

💰 5. Business Model Agent
Builds the revenue model and monetization strategy

Defines GTM (go-to-market) and scaling strategy

🎯 6. Pitch Composer Agent
Synthesizes outputs from all agents into a compelling, investor-ready startup pitch

🛠️ Tech Stack
LangGraph – Multi-agent workflow engine

Gemini 1.5 Flash – High-speed, high-context GenAI model

LangChain Community Tools – Search tools (DuckDuckGo)

Python – Core logic

Streamlit – Fast frontend UI

🧪 How It Works
User enters a startup idea via the Streamlit UI.

The LangGraph engine triggers each agent in a defined flow.

Agents collaborate, passing data between each other.

Final pitch is displayed in a clean, readable format.

🔥 Demo Use Case
Input: “AI tool that helps doctors summarize patient case histories”
Output: Market insights, founder profile, clear problem definition, innovative AI solution, monetization model, and an investor-ready pitch.



📦 Installation

git clone https://github.com/yourusername/startup-pitch-agent.git
cd startup-pitch-agent
pip install -r requirements.txt
streamlit run app.py



Make sure you have a .env file with your Gemini API key:

GOOGLE_API_KEY=your_key_here

🙌 Connect With Me
If you're passionate about GenAI, agentic workflows, or startup tooling, let’s collaborate!

📧 varunpadala137@gmail.com
