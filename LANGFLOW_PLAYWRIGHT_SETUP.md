# Langflow Playwright Setup Guide

This guide helps you check and install Playwright on your Langflow server so browser automation works.

## 🎯 Understanding the Setup

Your Streamlit app sends requests to Langflow → Langflow runs Playwright MCP → Browser automation happens **on the Langflow server**

```
Your Laptop                 Langflow Server (localhost:7860)
┌─────────────┐            ┌──────────────────────────────┐
│ Streamlit   │   HTTP     │  Langflow → Playwright MCP   │
│    App      │ ────────>  │           → Chromium         │
└─────────────┘            └──────────────────────────────┘
```

**Therefore:** Playwright must be installed on the **Langflow server**, not on your Streamlit app.

## 📋 Quick Start

### Step 1: Check Current Status

Run the checker script to see what's installed:

```bash
python check_langflow_playwright.py
```

This will check:
- ✅ Langflow server accessibility
- ✅ MCP settings endpoint
- ✅ Node.js installation
- ✅ Playwright availability
- ✅ Chromium browser
- ✅ Playwright MCP package

### Step 2: Install on Langflow Server

**If Langflow is running locally (localhost:7860):**

```bash
bash install_playwright_server.sh
```

**If Langflow is on a remote server:**

1. Copy the script to the server:
   ```bash
   scp install_playwright_server.sh user@server:/tmp/
   ```

2. SSH into the server and run:
   ```bash
   ssh user@server
   cd /tmp
   bash install_playwright_server.sh
   ```

### Step 3: Configure MCP in Langflow

1. Open Langflow settings: http://localhost:7860/settings/mcp-servers

2. Add a new MCP server:
   - **Name:** `playwright`
   - **Command:** `npx`
   - **Args:** `@playwright/mcp@latest`

3. Save the configuration

### Step 4: Restart Langflow

The Langflow server needs to be restarted to pick up the new MCP configuration:

```bash
# If running as a service
sudo systemctl restart langflow

# Or if running directly in terminal
# Stop the current process (Ctrl+C) and restart:
langflow run
```

### Step 5: Test Your Streamlit App

```bash
streamlit run streamlit_app.py
```

Send a test request that uses browser automation!

## 🔧 Manual Installation

If the script doesn't work, install manually on the Langflow server:

```bash
# 1. Install Node.js (if not installed)
# Ubuntu/Debian:
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS:
brew install node

# 2. Install Playwright and Chromium
npx playwright install chromium

# 3. Install system dependencies
npx playwright install-deps chromium

# 4. Verify installation
npx playwright --version
npx @playwright/mcp@latest --help

# 5. Test browser
node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  console.log('✅ Browser works!');
  await browser.close();
})();
"
```

## 🐛 Troubleshooting

### Error: "Cannot connect to Langflow server"

**Solution:** Start Langflow first:
```bash
langflow run
```

Then run the checker script again.

### Error: "Node.js is not installed"

**Solution:** Install Node.js on the **Langflow server**:

```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# macOS
brew install node

# Verify
node --version
npm --version
```

### Error: "Could not find browser"

**Solution:** Install Chromium browser:
```bash
npx playwright install chromium
npx playwright install-deps chromium
```

### Error: "libgobject-2.0.so.0: cannot open shared object file"

**Solution:** Install system dependencies:
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxcb1 \
    libxkbcommon0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2

# Or use Playwright's helper
npx playwright install-deps chromium
```

### Error: "Permission denied" when installing

**Solution:** Run with sudo or fix permissions:
```bash
# Option 1: Use sudo
sudo npx playwright install chromium

# Option 2: Install in user directory
npm config set prefix ~/.npm-global
export PATH=~/.npm-global/bin:$PATH
npx playwright install chromium
```

### MCP Server Not Showing in Langflow

**Solution:**
1. Check the configuration file directly:
   ```bash
   # Find Langflow config (location varies)
   find ~ -name "mcp_servers.json" 2>/dev/null
   cat /path/to/mcp_servers.json
   ```

2. Manually edit if needed:
   ```json
   {
     "servers": {
       "playwright": {
         "command": "npx",
         "args": ["@playwright/mcp@latest"]
       }
     }
   }
   ```

3. Restart Langflow after editing

### Browser Works Locally but Not on Server

**Solution:** For headless server environments:

```bash
# Install X virtual framebuffer
sudo apt-get install -y xvfb

# Run with virtual display
export DISPLAY=:99
Xvfb :99 -screen 0 1920x1080x24 &

# Or use Playwright's headless mode (recommended)
# This should work automatically in most cases
```

## 📊 Verification Commands

Run these on the **Langflow server** to verify everything is working:

```bash
# Check Node.js
node --version        # Should show v16+ or v18+

# Check npm
npm --version         # Should show version number

# Check Playwright
npx playwright --version

# Check Chromium installation
npx playwright install --dry-run chromium

# Test browser launch
node -e "
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('https://example.com');
  console.log('Title:', await page.title());
  await browser.close();
})();
"

# Test Playwright MCP
timeout 5 npx @playwright/mcp@latest --help
```

## 📁 Files Created

1. **`check_langflow_playwright.py`** - Diagnostic script to check installation status
2. **`install_playwright_server.sh`** - Automated installation script for Langflow server
3. **`LANGFLOW_PLAYWRIGHT_SETUP.md`** - This guide

## 🔗 Useful Links

- Playwright Documentation: https://playwright.dev/
- Playwright MCP: https://github.com/modelcontextprotocol/servers/tree/main/playwright
- Langflow Documentation: https://docs.langflow.org/
- Node.js Download: https://nodejs.org/

## 💡 Tips

- Run the checker script regularly to ensure everything stays working
- Keep Playwright updated: `npx playwright@latest install chromium`
- Monitor Langflow logs for MCP errors: `langflow run --log-level debug`
- Test with simple browser tasks first before complex automation
- Use `headless: true` mode on servers without displays

## 🎯 Next Steps

After installation:
1. ✅ Verify with checker script
2. ✅ Configure MCP in Langflow
3. ✅ Restart Langflow
4. ✅ Test with Streamlit app
5. ✅ Monitor for errors
6. ✅ Celebrate! 🎉

