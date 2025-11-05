#!/bin/bash
# Script to install Playwright on Langflow server
# Run this script on the server where Langflow is running

set -e  # Exit on error

echo "🚀 Installing Playwright for Langflow MCP..."
echo "================================================"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed!"
    echo "Please install Node.js first:"
    echo "  Ubuntu/Debian: curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash - && sudo apt-get install -y nodejs"
    echo "  macOS: brew install node"
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"

# Install Playwright
echo ""
echo "📦 Installing Playwright..."
npx -y playwright@latest install chromium

# Install system dependencies
echo ""
echo "📦 Installing system dependencies..."
if command -v apt-get &> /dev/null; then
    echo "Detected Debian/Ubuntu system"
    npx -y playwright install-deps chromium
elif command -v brew &> /dev/null; then
    echo "Detected macOS system"
    # Chromium is installed via npx playwright install
    echo "✅ Chromium installed via Playwright"
else
    echo "⚠️  Could not detect package manager. You may need to install dependencies manually."
fi

# Test installation
echo ""
echo "🧪 Testing Playwright installation..."
npx -y playwright --version

# Test Playwright MCP
echo ""
echo "🧪 Testing Playwright MCP package..."
npx -y @playwright/mcp@latest --help || echo "⚠️  Could not test @playwright/mcp"

echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Configure MCP server in Langflow at http://localhost:7860/settings/mcp-servers"
echo "2. Add server with command 'npx' and args ['@playwright/mcp@latest']"
echo "3. Restart Langflow to pick up the configuration"
