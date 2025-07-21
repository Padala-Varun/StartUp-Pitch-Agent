# 📁 startup_pitch_agent/app.py

import os
import streamlit as st
from dotenv import load_dotenv
from typing import TypedDict, Optional
from langgraph.graph import StateGraph

# Import all agent functions
from agents.input_agent import get_startup_idea
from agents.problem_agent import analyze_problem
from agents.solution_agent import generate_solution
from agents.market_agent import research_market
from agents.competitor_agent import analyze_competitors
from agents.format_agent import format_slides

# Define the state structure
class PitchState(TypedDict, total=False):
    idea: Optional[str]
    problem: Optional[str]
    solution: Optional[str]
    market: Optional[str]
    competitors: Optional[str]
    business_model: Optional[str]
    gtm_strategy: Optional[str]
    team: Optional[str]
    slides: Optional[list]

# ✅ Load API Keys
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ GOOGLE_API_KEY not found in .env file. Please set it.")
    st.stop()

# ✅ LangGraph setup
graph = StateGraph(PitchState)

# ➕ Add Nodes (Agents)
graph.add_node("Input", get_startup_idea)
graph.add_node("Problem", analyze_problem)
graph.add_node("Solution", generate_solution)
graph.add_node("Market", research_market)
graph.add_node("Competitors", analyze_competitors)

# ➕ Add Custom Logic Nodes
def build_business_model(state):
    idea = state.get("idea", "a startup")
    return {"business_model": f"The business model for {idea} is a SaaS subscription with free trials."}

def generate_gtm_strategy(state):
    idea = state.get("idea", "the startup")
    return {"gtm_strategy": f"The GTM strategy for {idea} includes Product Hunt launch, SEO, and tech influencer campaigns."}

def suggest_team(state):
    idea = state.get("idea", "a startup")
    return {"team": f"The ideal team for {idea} includes a full-stack engineer, growth marketer, and a domain expert."}

graph.add_node("BusinessModel", build_business_model)
graph.add_node("GTM", generate_gtm_strategy)
graph.add_node("Team", suggest_team)
graph.add_node("Formatter", format_slides)

# 🔁 Define Flow
graph.set_entry_point("Input")
graph.add_edge("Input", "Problem")
graph.add_edge("Problem", "Solution")
graph.add_edge("Solution", "Market")
graph.add_edge("Market", "Competitors")
graph.add_edge("Competitors", "BusinessModel")
graph.add_edge("BusinessModel", "GTM")
graph.add_edge("GTM", "Team")
graph.add_edge("Team", "Formatter")
graph.set_finish_point("Formatter")

# ✅ Compile the graph
app = graph.compile()

# 🌐 Streamlit UI
st.set_page_config(page_title="🚀 AI Startup Pitch Deck Generator", layout="centered")
st.title("🚀 Multi-Agent AI Startup Pitch Deck Generator")

# 👉 Input Box
idea = st.text_area("📌 Describe your startup idea:", height=150, placeholder="e.g., An AI tool that helps students summarize lectures.")

# 👉 Generate Button
if st.button("🎯 Generate Startup Pitch") and idea:
    with st.spinner("⏳ Agents are brainstorming..."):
        result = app.invoke({"idea": idea})

    st.success("✅ Pitch Deck Generated!")

    if result.get("slides"):
        st.markdown(result["slides"], unsafe_allow_html=True)

    else:
        st.warning("⚠️ No slides generated. Please try again with a more detailed idea.")
