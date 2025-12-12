# NY Times AI Chatbot

🤖 A sophisticated multi-agent AI chatbot that researches and analyzes New York Times articles using state-of-the-art LLM orchestration.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

- **Multi-Agent Architecture**: Specialized agents working together
  - **Research Agent**: Searches NY Times articles via official API
  - **Summarization Agent**: Creates factual summaries
  - **Critical Analyst Agent**: Provides deep analysis and insights
  - **Supervisor Agent**: Orchestrates the entire workflow

- **Powered by LangGraph**: Advanced agent orchestration framework
- **Beautiful Web Interface**: Streamlit-based UI
- **Structured Output**: Professional reports with three sections:
  1. Factual Summary
  2. Critical Analysis
  3. Source Articles with links

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- NY Times Developer API key ([Get it here](https://developer.nytimes.com/))
- OpenAI API key ([Get it here](https://platform.openai.com/))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/nytimes-ai-chatbot.git
   cd nytimes-ai-chatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## 🌐 Deploy to the Web

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on deploying to:
- Streamlit Cloud (FREE - Recommended)
- Render
- Railway
- Heroku

**Quick Deploy to Streamlit Cloud:**
1. Push code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and add API keys as secrets
4. Deploy! ✨

## 📝 Example Queries

```
What are the latest developments in space exploration, and write a paragraph explaining the commercial market opportunity?
```

```
Tell me about recent AI breakthroughs and their impact on the job market
```

```
Climate change policy updates from the last month and economic implications
```

## 🏗️ Architecture

```
User Query
    ↓
Supervisor Agent (Planning)
    ↓
Research Agent (NY Times API Search)
    ↓
Summarization Agent (Factual Summary)
    ↓
Critical Analyst Agent (Deep Analysis)
    ↓
Supervisor Agent (Compile Output)
    ↓
Structured Report
```

## 📁 Project Structure

```
nytimes-ai-chatbot/
├── app.py              # Streamlit web interface
├── cli.py              # Command line interface
├── orchestrator.py     # LangGraph workflow orchestration
├── agents.py           # Agent definitions
├── nyt_api.py         # NY Times API integration
├── config.py          # Configuration management
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment variables
└── README.md         # This file
```

## 🔧 Configuration

Environment variables (`.env` file):

```bash
# Required
NYT_API_KEY=your_nyt_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Optional
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.7
```

## 🔒 Security

- **No hardcoded credentials**: All API keys are loaded from environment variables
- **Secure by default**: `.env` files are gitignored
- **Best practices**: Following cryptographic security guidelines

## 📊 API Rate Limits

- **NY Times API**: 4,000 requests per day, 10 requests per minute (free tier)
- **OpenAI API**: Depends on your plan and model

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is for educational and research purposes. Make sure to comply with:
- NY Times API Terms of Service
- OpenAI API Terms of Use

## 🙏 Acknowledgments

- **New York Times** for their excellent API
- **LangChain & LangGraph** for the multi-agent framework
- **OpenAI** for GPT models
- **Streamlit** for the web framework

## 📞 Support

For issues:
- **NY Times API**: https://developer.nytimes.com/support
- **OpenAI API**: https://help.openai.com/

---

**Made with ❤️ using LangGraph and the NY Times API**
