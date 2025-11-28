# app/agents/architecture_agent.py

"""
───────────────────────────────────────────────────────────────
🏗️ ARCHITECTURE & DESIGN AGENT (Agno Framework)
───────────────────────────────────────────────────────────────
Purpose:
--------
This agent transforms a researched and validated idea into a
structured solution design or technical blueprint.

It suggests:
- System architecture or conceptual design
- Tech stack recommendations
- Data flow and module-level explanation
- (Optional) Mermaid architecture diagram
───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat

llm = OpenAIChat(id="gpt-4.1")

ArchitectureAgent = Agent(
    name="Architecture & Design Agent",
    description="""
        Converts the researched idea into a detailed system or
        solution architecture with component breakdown, data flow,
        and suggested technologies.
    """,
    instructions="""
        You are a senior solution architect and systems designer.

        Input: A JSON containing a validated idea, market data, and research info.

        Your tasks:
        1. Identify the system type (e.g., AI App, Web Platform, Mobile App).
        2. Use your tools to:
           - Generate a simple Mermaid diagram text
           - Suggest an appropriate technology stack
        3. Based on these, produce a structured JSON with:
           {
             "system_type": "...",
             "proposed_architecture": "Explain major components and their interactions.",
             "tech_stack": "Frontend: ..., Backend: ..., etc.",
             "architecture_diagram": "```mermaid ...```",
             "data_flow": "Explain how data moves through the system."
           }
        4. provide clear and detailed explanations for each section.
        5. Always output in valid JSON format — no text outside JSON.
    """,
    tools=[],
    model=llm,
)
