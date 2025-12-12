#!/bin/bash

echo "🔧 Fixing config.py for Streamlit Cloud compatibility..."
echo ""

cd "/Users/ishansingh/Downloads/NY Times AI Chatbot"

git add config.py
git commit -m "Fix: Update config.py to read from Streamlit secrets"
git push origin main

echo ""
echo "✅ Config fix pushed to GitHub!"
echo ""
echo "📋 What changed:"
echo "  - Removed Pydantic dependency issues"
echo "  - Added Streamlit secrets support (st.secrets)"
echo "  - Falls back to .env for local development"
echo ""
echo "🔄 Your Streamlit Cloud app should now redeploy automatically!"
echo ""
echo "⏱️  Wait 2-3 minutes and check the deployment logs."

