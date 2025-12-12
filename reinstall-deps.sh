#!/bin/bash

echo "🔧 Reinstalling Dependencies for Local Development"
echo "=================================================="
echo ""

cd "/Users/ishansingh/Downloads/NY Times AI Chatbot"

# Activate virtual environment
if [ -d ".venv" ]; then
    echo "✅ Found virtual environment"
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo "✅ Found virtual environment"
    source venv/bin/activate
else
    echo "📦 Creating new virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
fi

echo ""
echo "📥 Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ All dependencies installed successfully!"
    echo ""
    echo "🚀 You can now run the app:"
    echo "   streamlit run app.py"
    echo ""
else
    echo ""
    echo "❌ Installation failed. Try manually:"
    echo "   source .venv/bin/activate"
    echo "   pip install -r requirements.txt"
    echo ""
fi

