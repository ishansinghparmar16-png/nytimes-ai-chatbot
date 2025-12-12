# Quick Start Guide

## 🚀 Get Started in 3 Minutes

### Step 1: Setup
```bash
# Navigate to the project directory
cd "NY Times AI Chatbot"

# Run the setup script
./setup.sh
```

### Step 2: Configure API Keys

Edit the `.env` file:
```bash
# On Mac/Linux
nano .env

# Or use any text editor
```

Add your API keys:
```
NYT_API_KEY=your_actual_nyt_api_key_here
OPENAI_API_KEY=your_actual_openai_api_key_here
```

**Get API Keys:**
- NY Times: https://developer.nytimes.com/ → Register → Enable "Article Search API"
- OpenAI: https://platform.openai.com/ → API Keys → Create new key

### Step 3: Run the Chatbot

**Option A: Web Interface (Recommended)**
```bash
source venv/bin/activate
streamlit run app.py
```
Opens at http://localhost:8501

**Option B: Command Line**
```bash
source venv/bin/activate
python cli.py
```

## 📝 Example Query

Try this in the chatbot:
```
What are the latest developments in space exploration, and write a paragraph explaining the commercial market opportunity?
```

You'll get:
1. ✅ Factual summary from NY Times articles
2. ✅ Critical analysis of commercial opportunities
3. ✅ Direct links to source articles

## 🎯 Tips

- **Be specific**: More detailed queries get better results
- **Ask for analysis**: Queries like "explain the opportunity" or "analyze the impact" trigger the Critical Analyst Agent
- **Use context**: Mention timeframes, regions, or specific aspects

## ⚡ Troubleshooting

**"Configuration Error"**
→ Make sure `.env` file exists and has valid API keys

**"No articles found"**
→ Try broader search terms or different keywords

**Rate limits**
→ NY Times API: 10 requests/minute (free tier)

## 📊 What Happens Behind the Scenes

```
Your Query
    ↓
Supervisor Agent (plans workflow)
    ↓
Research Agent (searches NY Times)
    ↓
Summarization Agent (creates summary)
    ↓
Critical Analyst Agent (provides analysis)
    ↓
Supervisor Agent (compiles final report)
```

All agents are powered by GPT-4 and orchestrated using LangGraph!

---

**Need help?** Check the full README.md for detailed documentation.

