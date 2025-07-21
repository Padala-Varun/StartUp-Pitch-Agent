from typing import Optional
from langchain_core.tools import tool
from ddgs import DDGS


@tool
def format_slides(
    idea: Optional[str] = None,
    problem: Optional[str] = None,
    solution: Optional[str] = None,
    market: Optional[str] = None,
    competitors: Optional[str] = None,
    business_model: Optional[str] = None,
    gtm: Optional[str] = None,
    team: Optional[str] = None
) -> dict:
    """Formats all pitch components into a slide-style output and returns it as a dictionary."""

    def format_section(title: str, content: Optional[str]) -> str:
        return f"---\n### {title}\n{content or 'Content not available'}\n"

    slide_text = f"""
📌 **Startup Pitch Deck**

{format_section("💡 Idea", idea)}
{format_section("❗ Problem", problem)}
{format_section("✅ Solution", solution)}
{format_section("📊 Market Research", market)}
{format_section("🥊 Competitor Analysis", competitors)}
{format_section("💰 Business Model", business_model)}
{format_section("🚀 Go-To-Market Strategy", gtm)}
{format_section("👥 Suggested Team", team)}

---
🎯 **Thank You!**
Let's build something amazing.
"""

    return {"slides": slide_text}
