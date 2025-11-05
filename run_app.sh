#!/bin/bash
# Simple script to run the Streamlit app

echo "🚀 Starting Langflow Streamlit App..."
cd /Users/tansa/Downloads/langflow_streamlit

# Check if venv exists, if not create it
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "📥 Installing dependencies..."
    ./venv/bin/pip install -r requirements.txt
fi

# Run the app
./venv/bin/python -m streamlit run streamlit_app.py

