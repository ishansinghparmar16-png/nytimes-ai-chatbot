"""
Streamlit web interface for NY Times AI Chatbot.
"""
import streamlit as st
from orchestrator import run_chatbot
from config import settings
import os


# Page configuration
st.set_page_config(
    page_title="NY Times AI Chatbot",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        color: #1a1a1a;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #3498db;
        color: white;
        font-size: 1.1rem;
        padding: 0.75rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
</style>
""", unsafe_allow_html=True)


def main():
    """Main application interface."""
    
    # Header
    st.markdown('<div class="main-header">📰 NY Times AI Chatbot</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">Multi-Agent Research Assistant powered by NY Times API</div>',
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This chatbot uses a multi-agent system to:
        
        1. **Research Agent** - Searches NY Times articles
        2. **Summarization Agent** - Creates factual summaries
        3. **Critical Analyst Agent** - Provides deep analysis
        4. **Supervisor Agent** - Orchestrates the workflow
        
        ### How to Use
        Enter your query in the text area and click "Research & Analyze".
        
        ### Example Queries
        - "What are the latest developments in AI?"
        - "Climate change policy updates and economic impact"
        - "Space exploration and commercial opportunities"
        """)
        
        st.markdown("---")
        st.markdown("### Configuration")
        
        # Check API key status
        if settings.nyt_api_key and settings.nyt_api_key != "your_nyt_api_key_here":
            st.success("✅ NY Times API Key configured")
        else:
            st.error("❌ NY Times API Key not configured")
            
        if settings.openai_api_key and settings.openai_api_key != "your_openai_api_key_here":
            st.success("✅ OpenAI API Key configured")
        else:
            st.warning("⚠️ OpenAI API Key not configured")
        
        st.info(f"Model: {settings.llm_model}")
        st.info(f"Max Articles: {settings.max_articles_to_fetch}")
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("### 💬 Your Query")
        
    with col2:
        if st.button("🔄 Clear", help="Clear all inputs"):
            st.session_state.clear()
            st.rerun()
    
    # User input
    user_query = st.text_area(
        "Enter your research question:",
        placeholder="Example: What are the latest developments in renewable energy, and explain the investment opportunities?",
        height=100,
        key="query_input"
    )
    
    # Search button
    if st.button("🔍 Research & Analyze", type="primary"):
        if not user_query.strip():
            st.warning("⚠️ Please enter a query first.")
            return
            
        # Check if API keys are configured
        if not settings.nyt_api_key or settings.nyt_api_key == "your_nyt_api_key_here":
            st.error("❌ NY Times API Key is not configured. Please set it in your .env file.")
            return
            
        if not settings.openai_api_key or settings.openai_api_key == "your_openai_api_key_here":
            st.error("❌ OpenAI API Key is not configured. Please set it in your .env file.")
            return
        
        # Run the chatbot
        with st.spinner("🤖 Multi-agent system processing your query..."):
            try:
                result = run_chatbot(user_query)
                st.session_state.result = result
                st.session_state.query = user_query
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                return
    
    # Display results
    if "result" in st.session_state:
        st.markdown("---")
        
        # Parse and display the structured output
        result = st.session_state.result
        
        # Try to parse sections
        if "SECTION 1: FACTUAL SUMMARY" in result:
            sections = result.split("SECTION")
            
            # Display Summary Section
            if len(sections) > 1:
                st.markdown('<div class="section-header">📰 Factual Summary</div>', unsafe_allow_html=True)
                summary_section = sections[1].split("SECTION 2")[0] if len(sections) > 2 else sections[1]
                summary_text = summary_section.replace("1: FACTUAL SUMMARY", "").replace("-" * 80, "").strip()
                st.markdown(summary_text)
            
            # Display Analysis Section
            if len(sections) > 2:
                st.markdown('<div class="section-header">💡 Critical Analysis</div>', unsafe_allow_html=True)
                analysis_section = sections[2].split("SECTION 3")[0] if len(sections) > 3 else sections[2]
                analysis_text = analysis_section.replace("2: CRITICAL ANALYSIS", "").replace("-" * 80, "").strip()
                st.markdown(analysis_text)
            
            # Display Sources Section
            if len(sections) > 3:
                st.markdown('<div class="section-header">🔗 Source Articles</div>', unsafe_allow_html=True)
                sources_section = sections[3]
                sources_text = sources_section.replace("3: SOURCE ARTICLES", "").replace("-" * 80, "").replace("=" * 80, "").strip()
                st.markdown(sources_text)
        else:
            # Fallback: display raw output
            st.text(result)
        
        # Download button
        st.markdown("---")
        st.download_button(
            label="📥 Download Report",
            data=result,
            file_name="nyt_research_report.txt",
            mime="text/plain"
        )


if __name__ == "__main__":
    # Check if configuration is valid
    try:
        settings.validate_api_keys()
        main()
    except Exception as e:
        st.error(f"⚠️ Configuration Error: {e}")
        st.info("Please create a .env file based on .env.example and add your API keys.")
        
        # Show example .env content
        with st.expander("📝 Example .env file"):
            st.code("""
NYT_API_KEY=your_nyt_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.7
            """, language="bash")
        
        st.markdown("""
        ### How to get API keys:
        
        1. **NY Times API Key**: 
           - Visit https://developer.nytimes.com/
           - Create an account and register for the Article Search API
        
        2. **OpenAI API Key**:
           - Visit https://platform.openai.com/
           - Create an account and generate an API key
        """)

