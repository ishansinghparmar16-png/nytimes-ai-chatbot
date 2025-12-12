#!/bin/bash

# Quick fix for deployment issues
cd "/Users/ishansingh/Downloads/NY Times AI Chatbot"

echo "🔧 Fixing requirements.txt and pushing update..."
echo ""

git add requirements.txt
git commit -m "Fix: Update requirements.txt for Streamlit Cloud compatibility"
git push origin main

echo ""
echo "✅ Update pushed to GitHub!"
echo ""
echo "📋 Next steps:"
echo "1. Go to your Streamlit Cloud dashboard"
echo "2. Your app should automatically redeploy with the fix"
echo "3. If not, click 'Reboot' in the app menu"
echo ""
echo "The error was caused by strict version pinning."
echo "Now using flexible versions that work better with Streamlit Cloud."

