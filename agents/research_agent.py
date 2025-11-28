# app/agents/research_agent.py

"""
───────────────────────────────────────────────────────────────
📚 RESEARCH AGENT (Agno Framework)
───────────────────────────────────────────────────────────────
Purpose:
--------
This agent takes the structured idea output from the Idea Analyzer
and performs web and academic research to find relevant work,
existing projects, datasets, and papers.

It provides a research summary with references and insights,
which will later feed into Market Analysis and Architecture Agents.
───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.run.agent import RunOutput
from agno.tools.webbrowser import WebBrowserTools
from agno.tools.arxiv import ArxivTools
from agno.tools.serpapi import SerpApiTools
llm = OpenAIChat(id="gpt-4.1")
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────────────────────
# 🧩 Define the Agent
# ─────────────────────────────────────────────────────────────
ResearchAgent = Agent(
    name="Research Agent",
    description="""
        The Research Agent explores existing knowledge related to a structured idea.
        It gathers:
        - Academic papers and research insights
        - Existing startups, open-source projects, and tools
        - Public datasets and APIs
        - Relevant innovations and emerging trends
    """,
    instructions="""
        You are an expert research assistant with access to web and academic tools.

        Given a structured idea input (in JSON form), your tasks are:
        1. Extract the key topic, keywords, and domain from the idea.
        2. Use your tools to find:
           - 3–5 research papers or studies related to the idea
           - 3–5 existing products or startups solving similar problems
           - Any relevant public datasets or APIs
        3. Summarize your findings clearly and in a deatiled way under these sections:
           - Research Papers Summary
           - Existing Solutions
           - Available Datasets / APIs
           - Key Takeaways
        4. Return your response as valid JSON with this structure:
           {
             "research_papers": [ { "title": "...", "summary": "...", "link": "..." } ],
             "existing_projects": [ { "name": "...", "description": "...", "url": "..." } ],
             "datasets_or_apis": [ { "name": "...", "source": "..." } ],
             "key_insights": "Proper discursive paragraph summarizing what you learned."
           }

        Be factual, elaborative and discursive. Elaborate summary and description in proper detail. If information is not available, respond with an empty array [] for that section.
        Do NOT output explanations outside JSON.
    """,
    tools=[ArxivTools(), WebBrowserTools(), SerpApiTools()],
    model=llm,
    markdown=True
)

# idea_json = """
# {
#   "problem_statement": "Students often struggle to manage and organize their study time efficiently, leading to poor academic performance and increased stress.",
#   "proposed_solution": "An app that utilizes AI to help students organize and optimize their study schedules.",
#   "target_audience": "Students, particularly those in high school and college.",
#   "key_features": [
#     "AI-powered personalized study schedule recommendations",
#     "Task and subject prioritization",
#     "Reminders and notifications",
#     "Progress tracking",
#     "Study analytics and feedback"
#   ],
#   "domain": "Education, AI",
#   "expected_impact": "Improved academic performance, reduced stress, and better time management for students."
# } 
# """
# user_idea = f"Perform research based on this structured idea: {idea_json}"
# response: RunOutput = ResearchAgent.run(user_idea, stream=False)
# print(response.content)