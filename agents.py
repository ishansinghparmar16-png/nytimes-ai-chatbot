"""
Agent definitions for the NY Times AI Chatbot.
"""
from typing import Dict, List, Optional, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langgraph.graph import StateGraph, END
import operator
from nyt_api import NYTSearchTool, NYTArticle
from config import settings


# Define the state that will be passed between agents
class AgentState(TypedDict):
    """State shared across all agents in the workflow."""
    user_query: str
    research_results: Optional[str]
    articles: Optional[List[Dict]]
    summary: Optional[str]
    analysis: Optional[str]
    final_output: Optional[str]
    messages: Annotated[List[BaseMessage], operator.add]
    next_agent: Optional[str]


# Initialize LLM
llm = ChatOpenAI(
    model=settings.llm_model,
    temperature=settings.llm_temperature,
    api_key=settings.openai_api_key
)


class ResearchAgent:
    """Agent responsible for searching NY Times articles."""
    
    def __init__(self):
        self.nyt_tool = NYTSearchTool()
        
    def execute(self, state: AgentState) -> AgentState:
        """Search for relevant articles based on user query."""
        query = state["user_query"]
        
        print(f"\n🔍 Research Agent: Searching for '{query}'...")
        
        # Extract potential filters from query
        filters = {}
        if "space" in query.lower() or "exploration" in query.lower():
            filters["news_desk"] = "Science"
            
        # Search for articles
        articles = self.nyt_tool.search_articles(
            query=query,
            filters=filters if filters else None
        )
        
        if not articles:
            state["research_results"] = "No articles found for this query."
            state["articles"] = []
        else:
            # Format articles for processing
            state["research_results"] = self.nyt_tool.format_articles_for_llm(articles)
            state["articles"] = [article.to_dict() for article in articles]
            
            print(f"✅ Found {len(articles)} articles")
        
        state["next_agent"] = "summarization"
        return state


class SummarizationAgent:
    """Agent responsible for creating factual summaries."""
    
    def __init__(self):
        self.llm = llm
        
    def execute(self, state: AgentState) -> AgentState:
        """Create a factual summary from research results."""
        print("\n📝 Summarization Agent: Creating factual summary...")
        
        research_results = state.get("research_results", "")
        user_query = state["user_query"]
        
        if not research_results or research_results == "No articles found for this query.":
            state["summary"] = "No relevant information found in NY Times articles."
            state["next_agent"] = "critical_analyst"
            return state
        
        system_prompt = """You are a factual summarization agent for a NY Times research assistant.
Your job is to create a clear, objective summary of the key facts from the provided articles.

Rules:
- Focus on factual information only
- Combine information from multiple articles coherently
- Maintain journalistic objectivity
- Highlight the most important developments
- Keep the summary concise but comprehensive (2-3 paragraphs)
- Do NOT add your own opinions or analysis"""

        user_prompt = f"""User Query: {user_query}

Articles Found:
{research_results}

Please create a factual summary of the key developments related to the user's query."""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        state["summary"] = response.content
        state["next_agent"] = "critical_analyst"
        
        print("✅ Summary created")
        return state


class CriticalAnalystAgent:
    """Agent responsible for deeper analysis and insights."""
    
    def __init__(self):
        self.llm = llm
        
    def execute(self, state: AgentState) -> AgentState:
        """Provide critical analysis based on the user query and summary."""
        print("\n🎯 Critical Analyst Agent: Providing analysis...")
        
        user_query = state["user_query"]
        summary = state.get("summary", "")
        research_results = state.get("research_results", "")
        
        system_prompt = """You are a critical analyst agent with expertise in business strategy and market analysis.
Your job is to provide insightful analysis that goes beyond the facts.

Based on the user's query and the factual summary, you should:
- Identify implicit questions or analytical needs in the user's query
- Provide strategic insights and implications
- Analyze trends, opportunities, or challenges
- Offer expert commentary on the significance of the developments
- Be thoughtful and nuanced in your analysis

You have access to the original articles to inform your analysis."""

        user_prompt = f"""User Query: {user_query}

Factual Summary:
{summary}

Original Articles for Reference:
{research_results}

Please provide a thoughtful analysis that addresses any analytical aspects of the user's query. 
Pay special attention to phrases like "explain the opportunity," "analyze the impact," or "what does this mean for..."
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        state["analysis"] = response.content
        state["next_agent"] = "supervisor_compile"
        
        print("✅ Analysis completed")
        return state


class SupervisorAgent:
    """Agent that orchestrates the workflow and compiles final output."""
    
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.summarization_agent = SummarizationAgent()
        self.critical_analyst_agent = CriticalAnalystAgent()
        
    def plan(self, state: AgentState) -> AgentState:
        """Initial planning - delegates to research agent."""
        print("\n👔 Supervisor Agent: Delegating to Research Agent...")
        state["next_agent"] = "research"
        return state
    
    def compile_final_output(self, state: AgentState) -> AgentState:
        """Compile the final structured output."""
        print("\n👔 Supervisor Agent: Compiling final output...")
        
        summary = state.get("summary", "No summary available.")
        analysis = state.get("analysis", "No analysis available.")
        articles = state.get("articles", [])
        
        # Build structured output
        output_sections = []
        
        output_sections.append("=" * 80)
        output_sections.append("NY TIMES AI CHATBOT - RESEARCH REPORT")
        output_sections.append("=" * 80)
        
        output_sections.append("\n📰 SECTION 1: FACTUAL SUMMARY")
        output_sections.append("-" * 80)
        output_sections.append(summary)
        
        output_sections.append("\n\n💡 SECTION 2: CRITICAL ANALYSIS")
        output_sections.append("-" * 80)
        output_sections.append(analysis)
        
        output_sections.append("\n\n🔗 SECTION 3: SOURCE ARTICLES")
        output_sections.append("-" * 80)
        if articles:
            for i, article in enumerate(articles, 1):
                output_sections.append(f"\n{i}. {article['headline']}")
                output_sections.append(f"   Published: {article['pub_date']}")
                output_sections.append(f"   Link: {article['web_url']}")
        else:
            output_sections.append("No source articles available.")
            
        output_sections.append("\n" + "=" * 80)
        
        final_output = "\n".join(output_sections)
        state["final_output"] = final_output
        state["next_agent"] = None
        
        print("✅ Final output compiled")
        return state

