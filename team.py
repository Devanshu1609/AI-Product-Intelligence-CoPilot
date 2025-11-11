from agents.idea_analyser_agent import IdeaAnalyzerAgent
from agents.research_agent import ResearchAgent
from agents.market_analysis_agent import MarketImpactAgent
from agents.architecture_agent import ArchitectureAgent
from agents.structuring_agent import StructuringAgent
from agents.report_generation_agent import ReportGeneratorAgent

from agno.team import Team
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.run.agent import RunOutput

load_dotenv()

idea_intelligence_team = Team(
    name="IdeaIntelligenceTeam",
    description=(
        "A collaborative multi-agent AI team that transforms raw, unstructured ideas "
        "into fully researched, validated, and formatted reports or pitch documents. "
        "The system autonomously coordinates between specialized agents responsible for "
        "idea analysis, research, market validation, architecture design, document structuring, "
        "and final report generation."
    ),
    model = OpenAIChat(id="gpt-4.1"),
    members=[
        IdeaAnalyzerAgent,
        ResearchAgent,
        MarketImpactAgent,
        ArchitectureAgent,
        StructuringAgent,
        ReportGeneratorAgent
    ],
    instructions=[
        """
        You are **Idea Intelligence Team (IIT)** — an autonomous agentic AI system 
        designed to assist innovators, students, researchers, and founders in 
        transforming vague or scattered ideas into comprehensive, structured, 
        and presentation-ready reports.

        🧠 Your collective mission:
        - Understand and refine the user’s raw idea into a well-defined concept.
        - Conduct relevant academic, technical, and market research autonomously.
        - Assess feasibility, competitors, and real-world applicability.
        - Design high-level architecture and recommended tech stack.
        - Organize the findings into a logical report structure.
        - Generate a complete formatted report (PDF, DOCX, or Markdown) ready for submission.

        ⚙️ Operational Principles:
        - Collaborate seamlessly between team members, each agent focusing on its core domain.
        - Exchange and reuse intermediate outputs automatically — no user intervention needed.
        - Maintain data consistency, factual grounding, and professional formatting.
        - Ensure all final outputs are structured JSON objects and contain both insights and formatted results.
        - Prioritize clarity, depth, and usefulness for the target audience (students, startups, researchers).

        📄 Expected Deliverables:
        - A complete idea report with the following keys:
          {
            "idea_summary": "...",
            "research_summary": "...",
            "market_summary": "...",
            "architecture_summary": "...",
            "structure_summary": "...",
            "final_report": "path/to/generated/file",
            "confidence_score": 0.0–1.0
          }

        🎯 Output Goals:
        - Convert creativity into clarity.
        - Provide end-to-end intelligence from idea inception to presentation.
        - Produce final reports that meet hackathon, research, or startup standards.

        Act as a unified intelligence — divide tasks internally, 
        collaborate naturally, and return one cohesive final output.
        """
    ],
    markdown=True,
    show_members_responses=True,
    debug_mode=True
)


if __name__ == "__main__":
    user_input = """
    I have an idea for an AI platform that helps students and early-stage founders 
    transform rough project concepts into well-structured reports with research data, 
    architecture diagrams, and market validation insights.
    """

    print("\n🚀 Launching Idea Intelligence Team (Autonomous Mode)...\n")
    response: RunOutput = idea_intelligence_team.run(user_input, stream=False)
    print("\n✅ Idea Intelligence Team Completed Full Workflow:\n")
    print(response.content)
