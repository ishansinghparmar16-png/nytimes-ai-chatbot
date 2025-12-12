"""
Multi-agent orchestration using LangGraph.
"""
from typing import Dict
from langgraph.graph import StateGraph, END
from agents import (
    AgentState,
    SupervisorAgent,
    ResearchAgent,
    SummarizationAgent,
    CriticalAnalystAgent
)


def create_workflow() -> StateGraph:
    """Create the multi-agent workflow graph."""
    
    # Initialize agents
    supervisor = SupervisorAgent()
    research_agent = ResearchAgent()
    summarization_agent = SummarizationAgent()
    critical_analyst = CriticalAnalystAgent()
    
    # Create workflow graph
    workflow = StateGraph(AgentState)
    
    # Add nodes for each agent
    workflow.add_node("supervisor_plan", supervisor.plan)
    workflow.add_node("research", research_agent.execute)
    workflow.add_node("summarization", summarization_agent.execute)
    workflow.add_node("critical_analyst", critical_analyst.execute)
    workflow.add_node("supervisor_compile", supervisor.compile_final_output)
    
    # Define routing function
    def route_agent(state: AgentState) -> str:
        """Route to the next agent based on state."""
        next_agent = state.get("next_agent")
        
        if next_agent == "research":
            return "research"
        elif next_agent == "summarization":
            return "summarization"
        elif next_agent == "critical_analyst":
            return "critical_analyst"
        elif next_agent == "supervisor_compile":
            return "supervisor_compile"
        else:
            return END
    
    # Set entry point
    workflow.set_entry_point("supervisor_plan")
    
    # Add edges
    workflow.add_conditional_edges(
        "supervisor_plan",
        route_agent,
        {
            "research": "research",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        "research",
        route_agent,
        {
            "summarization": "summarization",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        "summarization",
        route_agent,
        {
            "critical_analyst": "critical_analyst",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        "critical_analyst",
        route_agent,
        {
            "supervisor_compile": "supervisor_compile",
            END: END
        }
    )
    
    workflow.add_conditional_edges(
        "supervisor_compile",
        route_agent,
        {
            END: END
        }
    )
    
    return workflow


def run_chatbot(user_query: str) -> str:
    """
    Run the multi-agent chatbot workflow.
    
    Args:
        user_query: The user's input query
        
    Returns:
        Final compiled output
    """
    # Create workflow
    workflow = create_workflow()
    app = workflow.compile()
    
    # Initialize state
    initial_state: AgentState = {
        "user_query": user_query,
        "research_results": None,
        "articles": None,
        "summary": None,
        "analysis": None,
        "final_output": None,
        "messages": [],
        "next_agent": None
    }
    
    # Run workflow
    print("\n" + "=" * 80)
    print("🤖 NY TIMES AI CHATBOT - Multi-Agent System")
    print("=" * 80)
    print(f"\n📥 User Query: {user_query}\n")
    
    final_state = app.invoke(initial_state)
    
    return final_state.get("final_output", "Error: No output generated")


if __name__ == "__main__":
    # Test the workflow
    test_query = "What are the latest developments in space exploration, and write a paragraph explaining the commercial market opportunity."
    
    result = run_chatbot(test_query)
    print("\n" + result)

