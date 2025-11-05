# Chromium Browser Setup for Streamlit

This guide explains how to install and configure Chromium browser for your Streamlit app.

## Quick Setup

### 1. **Local Development (macOS/Linux)**

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Install system dependencies (if needed)
playwright install-deps chromium
```

Or simply run:
```bash
bash install_playwright.sh
```

### 2. **Streamlit Cloud Deployment**

Streamlit Cloud will automatically:
- Install Python packages from `requirements.txt` (including `playwright`)
- Install system packages from `packages.txt` (including `chromium`)

Then you need to add a startup script to install Playwright browsers. Create/update your Streamlit config:

**Option A: Using a startup script in your app**

Add this to the beginning of your `streamlit_app.py`:

```python
import os
import subprocess

# Install Playwright browsers on first run
def install_playwright():
    try:
        subprocess.run(["playwright", "install", "chromium"], check=True)
        subprocess.run(["playwright", "install-deps", "chromium"], check=True)
        print("Playwright browsers installed successfully")
    except Exception as e:
        print(f"Warning: Could not install Playwright browsers: {e}")

# Only run once per deployment
if not os.path.exists("/tmp/playwright_installed"):
    install_playwright()
    open("/tmp/playwright_installed", "w").close()
```

**Option B: Using a bash script**

Create a `.streamlit/config.toml` file:
```toml
[server]
enableCORS = false
```

And run the installation as part of your deployment process.

### 3. **Docker Deployment**

Add to your `Dockerfile`:

```dockerfile
FROM python:3.11-slim

# Install system dependencies for Chromium
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium && \
    playwright install-deps chromium

# Copy your app
COPY . /app
WORKDIR /app

CMD ["streamlit", "run", "streamlit_app.py"]
```

## Files Created

1. **`requirements.txt`** - Updated to include `playwright>=1.40.0`
2. **`packages.txt`** - System packages for Streamlit Cloud (chromium, chromium-driver)
3. **`install_playwright.sh`** - Bash script to install Playwright browsers locally

## Using Playwright in Your App

Here's a simple example of using Playwright in your Streamlit app:

```python
import streamlit as st
from playwright.sync_api import sync_playwright

def capture_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        screenshot = page.screenshot()
        browser.close()
        return screenshot

st.title("Web Screenshot Tool")
url = st.text_input("Enter URL", "https://www.example.com")

if st.button("Capture"):
    with st.spinner("Capturing screenshot..."):
        screenshot = capture_screenshot(url)
        st.image(screenshot)
```

## Troubleshooting

### Issue: "Executable doesn't exist"

**Solution**: Run `playwright install chromium` after installing the Python package.

### Issue: "libgobject-2.0.so.0: cannot open shared object file"

**Solution**: Install system dependencies:
```bash
playwright install-deps chromium
```

### Issue: Chromium crashes on Streamlit Cloud

**Solution**: Use `headless=True` mode and add these launch arguments:
```python
browser = p.chromium.launch(
    headless=True,
    args=['--no-sandbox', '--disable-setuid-sandbox']
)
```

### Issue: Permission denied on Streamlit Cloud

**Solution**: Set the browser path explicitly:
```python
browser = p.chromium.launch(
    headless=True,
    executable_path='/usr/bin/chromium',
    args=['--no-sandbox', '--disable-setuid-sandbox']
)
```

## Environment Variables

For production deployments, you may want to set:

```bash
export PLAYWRIGHT_BROWSERS_PATH=/path/to/browsers
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1  # If browsers are pre-installed
```

## Testing the Installation

Run this command to verify Chromium is installed:

```bash
playwright install --dry-run chromium
```

Or test in Python:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.example.com")
    print("Success! Chromium is working.")
    browser.close()
```

## Notes

- Chromium installation adds ~150-300MB to your deployment
- First launch may be slower as browsers initialize
- On Streamlit Cloud, use headless mode and disable sandboxing
- Your current app uses Playwright MCP on the server side, which is different from running Playwright directly in Streamlit

## Current App Architecture

Your app currently sends requests to a **Langflow API** that runs Playwright MCP server-side using:
```python
"command": "npx",
"args": ["@playwright/mcp@latest"]
```

This means the browser runs on the Langflow server, not in Streamlit. If you want to run browser automation directly in your Streamlit app, you'll need to refactor to use Playwright directly instead of calling the Langflow API.

