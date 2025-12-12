#!/bin/bash

# Setup script for NY Times AI Chatbot

echo "🤖 NY Times AI Chatbot - Setup Script"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

echo "✅ Python is installed"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Failed to create virtual environment"
    exit 1
fi

echo "✅ Virtual environment created"
echo ""

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env file and add your API keys!"
    echo ""
    echo "You need:"
    echo "  1. NY Times API Key from: https://developer.nytimes.com/"
    echo "  2. OpenAI API Key from: https://platform.openai.com/"
    echo ""
else
    echo "✅ .env file exists"
    echo ""
fi

echo "======================================"
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Edit .env file with your API keys"
echo "  2. Activate virtual environment: source venv/bin/activate"
echo "  3. Run web interface: streamlit run app.py"
echo "  4. OR run CLI: python cli.py"
echo ""
echo "Happy researching! 📰"

