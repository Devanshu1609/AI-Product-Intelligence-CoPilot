# app/agents/report_generator_agent.py

"""
───────────────────────────────────────────────────────────────
📝 REPORT GENERATOR AGENT (Agno Framework)
───────────────────────────────────────────────────────────────
Purpose:
--------
Generates the final formatted report based on all previous agents’
outputs and the structured outline from the Structuring Agent.

Supports multiple report types:
- Hackathon Project Report
- Research Scholar Report
- Startup Pitch
- Ideathon Presentation
───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Initialize model
llm = OpenAIChat(id="gpt-4.1")

# ─────────────────────────────────────────────────────────────
# 🧩 Agent Definition
# ─────────────────────────────────────────────────────────────
ReportGeneratorAgent = Agent(
    name="Report Generator Agent",
    description="""
        Synthesizes all agent outputs (Idea, Research, Market, Architecture, Structure)
        into a final human-readable formatted report. Supports export to PDF and DOCX.
    """,
    instructions="""
        You are a professional report composer and technical writer.

        Input:
        - Aggregated agent outputs (idea, research, market, architecture, structure)
        - report_type (hackathon / research / startup_pitch / ideathon)
        - desired_format (markdown / pdf / docx)

        Your job:
        1. Read the structured sections from the Structuring Agent.
        2. For each section:
            - Retrieve relevant data from other agents.
            - Generate clean, detailed, discursive, professional content.
        3. Maintain tone appropriate to the report type:
            - Hackathon: Energetic, concise, project-oriented.
            - Research: Formal, citation-ready, analytical.
            - Startup Pitch: Persuasive, visionary, data-driven.
            - Ideathon: Creative, innovation-focused.
        4. Generate the entire report as formatted Markdown text.

        Example output structure:
        {
          "report_type": "...",
          "format": "pdf / markdown / docx",
          "content": "## Title\\n ... markdown report ...",
          "export_status": "✅ PDF successfully generated: final_report.pdf"
        }



        RULES:
        - Always return valid JSON.
        - Summarize and format data clearly and in detail.
        - Include subheadings, bullets, and numbered sections where relevant.
        - Avoid repetition between sections.
    """,
    model=llm,
    markdown=True
)
