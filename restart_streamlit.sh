#!/bin/bash
# Script to restart Streamlit with clean cache

echo "🔄 Restarting Streamlit with fresh metadata..."
echo "=" * 60

# Clear Python cache
echo "1️⃣ Clearing Python cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete 2>/dev/null
echo "✅ Cache cleared"
echo

# Activate venv
echo "2️⃣ Activating virtual environment..."
source venv/bin/activate
echo "✅ Environment activated"
echo

# Verify metadata
echo "3️⃣ Verifying metadata..."
python3 -c "from mcp_tools_metadata import MCP_TOOLS_METADATA; print(f'✅ Loaded {len(MCP_TOOLS_METADATA)} tools')"
echo

# Kill any existing Streamlit processes
echo "4️⃣ Stopping any running Streamlit instances..."
pkill -f "streamlit run" 2>/dev/null
sleep 2
echo "✅ Previous instances stopped"
echo

# Start Streamlit
echo "5️⃣ Starting Streamlit..."
echo "=" * 60
streamlit run streamlit_app.py

