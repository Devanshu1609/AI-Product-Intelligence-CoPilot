# app/agents/idea_analyzer_agent.py

"""
───────────────────────────────────────────────────────────────
🤖 IDEA ANALYZER AGENT (Agno Framework)
───────────────────────────────────────────────────────────────
Purpose:
--------
This agent takes a raw, unstructured idea description from a user 
(e.g., “I want to build an AI app that helps farmers detect crop diseases.”)
and transforms it into a well-structured, detailed summary 
that clearly defines the problem, solution, target users, and other
key attributes.

It acts as the **foundation** for the multi-agent system —
subsequent agents (Research, Market, Architecture, etc.) rely on
its structured output.

───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.run.agent import RunOutput

# Initialize the LLM model
# You can replace this with Gemini, Claude, or Ollama
llm = OpenAIChat(id="gpt-4.1")

# ─────────────────────────────────────────────────────────────
# 🧠 Define the Agent
# ─────────────────────────────────────────────────────────────
IdeaAnalyzerAgent = Agent(
    name="Idea Analyzer Agent",
    description="""
        The Idea Analyzer Agent takes a raw idea or concept provided by the user
        and extracts structured information including:
        - Problem Statement
        - Proposed Solution
        - Target Audience
        - Key Features or Goals
        - Domain/Category
        - Expected Impact

        The agent must output its result in a clean JSON structure that will
        serve as the foundation for all subsequent agents.
    """,
    tools=[GoogleSearchTools(
        enable_google_search=True,
    )],
    instructions="""
        You are an expert product and research analyst.
        Your job is to analyze a user's raw, messy, or incomplete idea
        and return a clear, structured breakdown.

        Follow these rules strictly:
        1. Read the user's input carefully.
        2. Identify the core **problem statement** (what issue the idea is solving).
        3. Identify the **proposed solution** (what the user wants to create).
        4. Identify the **target audience** or beneficiaries.
        5. Extract key **features or goals** from the description.
        6. Determine the **domain or category** (Education, AI, Healthcare, etc.).
        7. Estimate the **expected impact or benefit**.
        8. Use your tools to research any unclear aspects of the idea.
        9. Output the response ONLY as a JSON object with the following keys:
           - problem_statement
           - proposed_solution
           - target_audience
           - key_features
           - domain
           - expected_impact

        Do NOT add explanations, notes, or comments — only return valid JSON.
    """,
    model=llm,
    markdown=True
)

# user_idea = "I want to make an app that helps students organize their study time using AI."
# response: RunOutput = IdeaAnalyzerAgent.run(user_idea, stream=False)
# print(response.content)