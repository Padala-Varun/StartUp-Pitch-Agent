from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

def analyze_competitors(state):
    query = f"Top competitors in {state['idea']} space"
    search_result = search.run(query)  # ✅ Use `.run()` not `.search()`
    return {"competitors": search_result, **state}
