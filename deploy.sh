#!/bin/bash

# Quick Deployment Script for Streamlit Cloud
# This script helps you push your code to GitHub

echo "🚀 NY Times AI Chatbot - Deployment Helper"
echo "=========================================="
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git initialized"
else
    echo "✅ Git repository already exists"
fi

# Add all files
echo ""
echo "📝 Adding files to git..."
git add .

# Check for changes
if git diff-index --quiet HEAD --; then
    echo "ℹ️  No changes to commit"
else
    echo ""
    echo "💾 Committing changes..."
    git commit -m "Prepare for deployment"
    echo "✅ Changes committed"
fi

echo ""
echo "=========================================="
echo "📋 Next Steps:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   → Go to https://github.com/new"
echo "   → Name it: nytimes-ai-chatbot"
echo "   → Keep it PUBLIC"
echo "   → Don't initialize with README"
echo ""
echo "2. Connect your repository (replace YOUR_USERNAME):"
echo "   git remote add origin https://github.com/YOUR_USERNAME/nytimes-ai-chatbot.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy on Streamlit Cloud:"
echo "   → Go to https://streamlit.io/cloud"
echo "   → Sign in with GitHub"
echo "   → Click 'New app'"
echo "   → Select your repository"
echo "   → Set Main file: app.py"
echo "   → Click 'Advanced settings'"
echo "   → Add secrets (see below)"
echo ""
echo "4. Add these secrets in TOML format:"
echo "   NYT_API_KEY = \"your_key_here\""
echo "   OPENAI_API_KEY = \"your_key_here\""
echo "   LLM_MODEL = \"gpt-4-turbo-preview\""
echo ""
echo "=========================================="
echo "✨ Your app will be live at:"
echo "   https://YOUR_USERNAME-nytimes-ai-chatbot.streamlit.app"
echo ""

