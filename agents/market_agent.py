import os
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

def research_market(state):
    query = f"Market size and growth for {state['idea']}"
    result = search.run(query)  # ✅ Correct method
    return {"market": result, **state}
