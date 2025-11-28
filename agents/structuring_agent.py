# app/agents/structuring_agent.py

"""
───────────────────────────────────────────────────────────────
🧩 STRUCTURING AGENT (Agno Framework)
───────────────────────────────────────────────────────────────
Purpose:
--------
This agent organizes the multi-agent outputs into a structured
outline or skeleton based on the target report type.

Supported formats:
- Hackathon Report
- Research Scholar Report
- Startup Pitch
- Ideathon Pitch
───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.serpapi import SerpApiTools
from agno.tools.webbrowser import WebBrowserTools

llm = OpenAIChat(id="gpt-4.1")

StructuringAgent = Agent(
    name="Structuring Agent",
    description="""
        Organizes and formats all previous agent outputs into
        a coherent, purpose-driven report or presentation structure.
    """,
    instructions="""
        You are an expert report designer and information architect.

        Input:
        - Aggregated data from previous agents (idea, research, market, architecture)
        - Desired report type (hackathon, research, startup_pitch, ideathon)

        Your goal:
        To generate a JSON structure defining sections, sub-sections,
        and the logical flow of the report. Do NOT fill in content.

        Use your tools to fetch common structures and best practices.

        Return structure in this format:
        {
          "report_type": "hackathon / research / startup_pitch / ideathon",
          "title": "Auto-generated from idea title",
          "sections": [
            {"heading": "Section 1 Title", "description": "Brief description"},
            {"heading": "Section 2 Title", "description": "Brief description"},
            ...
          ]
        }

        Below are the detailed guidelines for each type 👇

        ───────────────────────────────
        🧩 HACKATHON PROJECT REPORT
        ───────────────────────────────
        1. Introduction
        2. Problem Statement
        3. Proposed Solution
        4. Tech Stack & Architecture
        5. Implementation Details
        6. Challenges Faced
        7. Results & Impact
        8. Future Enhancements
        9. Team & Contributors

        ───────────────────────────────
        🎓 RESEARCH SCHOLAR REPORT
        ───────────────────────────────
        1. Abstract
        2. Introduction & Background
        3. Literature Review
        4. Problem Definition
        5. Methodology / System Design
        6. Experimental Results / Findings
        7. Discussion
        8. Conclusion
        9. References

        ───────────────────────────────
        🚀 STARTUP PITCH STRUCTURE
        ───────────────────────────────
        1. Problem
        2. Solution
        3. Market Opportunity
        4. Product Overview
        5. Business Model
        6. Competitive Advantage
        7. Traction / Metrics
        8. Financial Projection
        9. Team
        10. Ask / Funding Requirement

        ───────────────────────────────
        💡 IDEATHON REPORT STRUCTURE
        ───────────────────────────────
        1. Idea Overview
        2. Innovation Factor
        3. Problem Solved
        4. Target Audience
        5. Solution Approach
        6. Implementation Feasibility
        7. Impact & Use Cases
        8. Team & Collaboration
        9. Future Scope

        ───────────────────────────────
        RULES:
        - Select the structure based on report_type.
        - Include descriptions for each section.
        - Maintain logical flow and avoid duplication.
        - Output ONLY JSON.
    """,
    tools=[WebBrowserTools(), SerpApiTools()],
    model=llm,
    markdown=True
)
