#!/usr/bin/env python3
"""
Script to check and verify Playwright MCP installation on Langflow server
"""

import requests
import json
import subprocess
import sys
from typing import Dict, Any

# Langflow server configuration
LANGFLOW_BASE_URL = "http://localhost:7860"
MCP_SETTINGS_URL = f"{LANGFLOW_BASE_URL}/settings/mcp-servers"
API_URL = f"{LANGFLOW_BASE_URL}/api/v1"

def check_langflow_server():
    """Check if Langflow server is accessible"""
    print("=" * 60)
    print("🔍 Checking Langflow Server Connection...")
    print("=" * 60)
    
    try:
        response = requests.get(LANGFLOW_BASE_URL, timeout=5)
        print(f"✅ Langflow server is accessible at {LANGFLOW_BASE_URL}")
        print(f"   Status Code: {response.status_code}")
        return True
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot connect to Langflow server at {LANGFLOW_BASE_URL}")
        print("   Make sure Langflow is running!")
        return False
    except Exception as e:
        print(f"❌ Error connecting to Langflow: {e}")
        return False

def check_mcp_settings():
    """Check MCP server settings via API"""
    print("\n" + "=" * 60)
    print("🔍 Checking MCP Server Settings...")
    print("=" * 60)
    
    try:
        response = requests.get(MCP_SETTINGS_URL, timeout=5)
        if response.status_code == 200:
            print(f"✅ MCP settings endpoint is accessible")
            try:
                data = response.json()
                print(f"   Response: {json.dumps(data, indent=2)}")
            except:
                print(f"   Response (text): {response.text[:200]}")
        else:
            print(f"⚠️  MCP settings returned status: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
        return True
    except requests.exceptions.ConnectionError:
        print(f"❌ Cannot access MCP settings at {MCP_SETTINGS_URL}")
        return False
    except Exception as e:
        print(f"❌ Error checking MCP settings: {e}")
        return False

def check_local_nodejs():
    """Check if Node.js is installed locally"""
    print("\n" + "=" * 60)
    print("🔍 Checking Local Node.js Installation...")
    print("=" * 60)
    
    try:
        node_version = subprocess.check_output(["node", "--version"], 
                                              stderr=subprocess.STDOUT,
                                              text=True).strip()
        print(f"✅ Node.js is installed: {node_version}")
        
        npm_version = subprocess.check_output(["npm", "--version"],
                                             stderr=subprocess.STDOUT,
                                             text=True).strip()
        print(f"✅ npm is installed: {npm_version}")
        return True
    except FileNotFoundError:
        print("❌ Node.js is not installed on this machine")
        print("   Install from: https://nodejs.org/")
        return False
    except Exception as e:
        print(f"❌ Error checking Node.js: {e}")
        return False

def check_local_playwright():
    """Check if Playwright is installed locally"""
    print("\n" + "=" * 60)
    print("🔍 Checking Local Playwright Installation...")
    print("=" * 60)
    
    try:
        # Check if playwright is available
        result = subprocess.run(
            ["npx", "playwright", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✅ Playwright is available: {result.stdout.strip()}")
            
            # Check if Chromium is installed
            print("\n   Checking Chromium installation...")
            check_result = subprocess.run(
                ["npx", "playwright", "install", "--dry-run", "chromium"],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if "is already installed" in check_result.stdout or check_result.returncode == 0:
                print("   ✅ Chromium browser is installed")
            else:
                print("   ⚠️  Chromium browser may not be installed")
                print(f"   Output: {check_result.stdout}")
            
            return True
        else:
            print("⚠️  Playwright command failed")
            print(f"   Error: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ npx command not found")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Playwright check timed out")
        return False
    except Exception as e:
        print(f"❌ Error checking Playwright: {e}")
        return False

def check_playwright_mcp():
    """Check if Playwright MCP is available"""
    print("\n" + "=" * 60)
    print("🔍 Checking Playwright MCP Package...")
    print("=" * 60)
    
    try:
        # Try to get package info
        result = subprocess.run(
            ["npm", "view", "@playwright/mcp", "version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ @playwright/mcp is available on npm: v{version}")
            return True
        else:
            print("⚠️  Could not fetch @playwright/mcp info from npm")
            return False
            
    except Exception as e:
        print(f"❌ Error checking Playwright MCP: {e}")
        return False

def test_playwright_locally():
    """Test running a simple Playwright command locally"""
    print("\n" + "=" * 60)
    print("🧪 Testing Playwright Execution Locally...")
    print("=" * 60)
    
    try:
        # Try to run a simple Playwright test
        code = """
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://www.example.com');
  console.log('✅ Successfully loaded page:', await page.title());
  await browser.close();
})();
"""
        
        result = subprocess.run(
            ["node", "-e", code],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print("✅ Playwright can execute successfully!")
            print(f"   {result.stdout.strip()}")
            return True
        else:
            print("❌ Playwright execution failed")
            print(f"   Error: {result.stderr}")
            
            if "Could not find browser" in result.stderr:
                print("\n   💡 Solution: Install Chromium browser:")
                print("      npx playwright install chromium")
            
            return False
            
    except FileNotFoundError:
        print("❌ Node.js not available")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Playwright test timed out (might still be working)")
        return False
    except Exception as e:
        print(f"❌ Error testing Playwright: {e}")
        return False

def generate_installation_guide():
    """Generate installation instructions"""
    print("\n" + "=" * 60)
    print("📋 Installation Guide for Langflow Server")
    print("=" * 60)
    
    guide = """
To install Playwright on the Langflow server, SSH into the server and run:

1️⃣  Install Node.js (if not installed):
    # Ubuntu/Debian
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
    
    # Or macOS
    brew install node

2️⃣  Install Playwright and Chromium:
    npx playwright install chromium
    
3️⃣  Install system dependencies:
    # Ubuntu/Debian
    npx playwright install-deps chromium
    
    # Or manually
    sudo apt-get install -y chromium-browser chromium-chromedriver

4️⃣  Verify installation:
    npx playwright --version
    npx @playwright/mcp@latest --help

5️⃣  Test Playwright MCP:
    # This should start the MCP server
    npx @playwright/mcp@latest

6️⃣  Configure in Langflow:
    - Go to: http://localhost:7860/settings/mcp-servers
    - Add server with:
      Command: npx
      Args: ["@playwright/mcp@latest"]

7️⃣  Restart Langflow:
    # The service needs to pick up the new MCP configuration

📝 For headless server environments, you may need:
    export PLAYWRIGHT_BROWSERS_PATH=/path/to/browsers
    export DISPLAY=:99  # If running in X virtual framebuffer
"""
    
    print(guide)

def generate_install_script():
    """Generate a bash script for server installation"""
    script_path = "/Users/tansa/Desktop/langflow_streamlit/install_playwright_server.sh"
    
    script_content = """#!/bin/bash
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
"""
    
    try:
        with open(script_path, 'w') as f:
            f.write(script_content)
        subprocess.run(["chmod", "+x", script_path], check=True)
        print(f"\n✅ Created installation script: {script_path}")
        print(f"   Copy this to your Langflow server and run it!")
    except Exception as e:
        print(f"\n❌ Error creating script: {e}")

def main():
    """Main execution"""
    print("\n" + "=" * 60)
    print("   🎭 Langflow Playwright Checker & Installer")
    print("=" * 60)
    print()
    
    results = {
        "langflow_accessible": check_langflow_server(),
        "mcp_settings": check_mcp_settings(),
        "nodejs_installed": check_local_nodejs(),
        "playwright_available": check_local_playwright(),
        "playwright_mcp": check_playwright_mcp(),
    }
    
    # Only test locally if everything is installed
    if results["nodejs_installed"] and results["playwright_available"]:
        results["playwright_works"] = test_playwright_locally()
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)
    
    for check, result in results.items():
        status = "✅" if result else "❌"
        print(f"{status} {check.replace('_', ' ').title()}")
    
    # Recommendations
    print("\n" + "=" * 60)
    print("💡 Recommendations")
    print("=" * 60)
    
    if not results["langflow_accessible"]:
        print("• Start Langflow server first: langflow run")
    
    if not results["nodejs_installed"]:
        print("• Install Node.js from: https://nodejs.org/")
    
    if results["nodejs_installed"] and not results["playwright_available"]:
        print("• Install Playwright: npx playwright install chromium")
    
    if results["nodejs_installed"] and results["playwright_available"]:
        if not results.get("playwright_works", False):
            print("• Install Chromium: npx playwright install chromium")
            print("• Install dependencies: npx playwright install-deps chromium")
    
    # Generate installation resources
    generate_installation_guide()
    generate_install_script()
    
    print("\n" + "=" * 60)
    print("✨ Check complete!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)

