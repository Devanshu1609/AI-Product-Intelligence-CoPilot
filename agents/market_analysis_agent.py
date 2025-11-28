# app/agents/market_impact_agent.py

"""
───────────────────────────────────────────────────────────────
📈 MARKET & IMPACT AGENT (Agno Framework)
───────────────────────────────────────────────────────────────
Purpose:
--------
This agent evaluates the real-world feasibility, demand, and
potential impact of the analyzed idea.

It considers:
- Current market trends
- Existing competitors or similar solutions
- Target market demographics
- Societal or business impact

It then returns a detailed market summary that feeds the next agent:
(Architecture & Design Agent)
───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.webbrowser import WebBrowserTools
from agno.tools.serpapi import SerpApiTools

# Initialize LLM model
llm = OpenAIChat(id="gpt-4.1")

# ─────────────────────────────────────────────────────────────
# 🧩 Define Agent
# ─────────────────────────────────────────────────────────────
MarketImpactAgent = Agent(
    name="Market & Impact Agent",
    description="""
        The Market & Impact Agent evaluates the market demand,
        competition, target audience, and overall feasibility
        of the idea using online trend and company data.
    """,
    instructions="""
        You are a skilled business and technology market analyst.

        Input: A structured idea enriched with research outputs.
        You must:
        1. Identify the **core industry/domain** from the input.
        2. Use your tools
           to gather:
            - Market demand signals
            - Existing competitors
        3. Analyze:
            - Market opportunity (size & growth)
            - Key differentiators
            - Feasibility and risks
            - Target audience size and type
            - Potential social/economic impact
        4. Return a structured JSON like this:
           {
             "market_trends": "Summary of popularity and user demand",
             "competitors": [ {"name": "...", "url": "..."} ],
             "target_market": "Detailed summary of audience and region",
             "feasibility_analysis": "Discuss strengths, risks, and adoption potential",
             "expected_impact": "Predicted positive social/economic effects"
           }

        Be objective and data-driven. Use the results of your tools.
        Keep it factual and detailed. Only return valid JSON output.
    """,
    tools=[WebBrowserTools(), SerpApiTools()],
    model=llm,
    markdown=True
)
