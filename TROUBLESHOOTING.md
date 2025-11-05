# Troubleshooting: Slow Response Times

## 🐌 Problem: Simple Messages Taking >50 Seconds

### Root Cause
Your app was **always sending MCP Tools configuration** with every request, even for simple "Hello" messages. This caused:

1. ❌ **MCP Server initialization** on every request (`npx @playwright/mcp@latest`)
2. ❌ **First-time package download** (~10-30 seconds)
3. ❌ **Agent tool evaluation overhead** - considering browser tools even when not needed
4. ❌ **Payload bloat** - Sending 6 browser tool definitions unnecessarily

### ✅ Solution Implemented

**Fixed the "Simplified Mode" toggle** in `streamlit_app.py`:
- When **enabled** ✅ → No MCP tools sent, fast responses (5-10 seconds)
- When **disabled** → Full browser automation available (slower but powerful)

## 🚀 How to Use

### For Simple Chat (Fast)
1. Open Streamlit app
2. **Enable "🚀 Simplified Mode"** checkbox in sidebar
3. Send message → Get response in **5-10 seconds** ⚡

### For Browser Automation (Slower)
1. Open Streamlit app  
2. **Disable "🚀 Simplified Mode"** checkbox
3. Send browser commands → Response in **30-90 seconds** 🌐

## 🧪 Testing Tools Created

### 1. Quick Response Time Test
```bash
source venv/bin/activate
python test_simple_request.py
```

This sends a minimal request without MCP tools. Should respond in **5-10 seconds**.

### 2. Full System Check
```bash
source venv/bin/activate
python check_langflow_playwright.py
```

Comprehensive diagnostic of your Langflow + Playwright setup.

## 📊 Expected Response Times

| Request Type | Simplified Mode | Expected Time |
|-------------|----------------|---------------|
| Simple chat ("Hello") | ✅ ON | 5-10 seconds |
| Simple chat ("Hello") | ❌ OFF | 30-60 seconds (initializing MCP) |
| Browser automation | ❌ OFF | 30-90 seconds |
| Complex multi-step | ❌ OFF | 1-3 minutes |

## 🔧 What Changed in Code

**Before:**
```python
payload = {
    "tweaks": {
        "MCPTools-qmP5R": { ... }  # Always included
    }
}
```

**After:**
```python
payload = {
    "tweaks": { ... }
}

# Only add MCP Tools if NOT in simplified mode
if not simplified_mode:
    payload["tweaks"]["MCPTools-qmP5R"] = { ... }
```

## 💡 Best Practices

1. **Use Simplified Mode for:**
   - Testing connectivity
   - Simple Q&A
   - Text generation
   - Quick iterations

2. **Use Full Mode (MCP Tools) for:**
   - Web scraping
   - Browser automation
   - Taking screenshots
   - Interacting with web pages

3. **First Request After Restart:**
   - First MCP request will be slowest (initialization)
   - Subsequent requests are faster (server stays warm)

## 🐛 If Still Slow

### Check 1: Verify Simplified Mode is Working
Look at the "View Sent Payload" section in Streamlit response:
- **Simplified:** No `MCPTools-qmP5R` key
- **Full:** Has `MCPTools-qmP5R` with all tools

### Check 2: Test Gemini API Directly
```bash
curl -X POST http://localhost:7860/api/v1/run/YOUR-FLOW-ID \
  -H "Content-Type: application/json" \
  -d '{"input_value": "Hello", "output_type": "chat"}'
```

Should respond quickly.

### Check 3: Restart Langflow
```bash
# Stop Langflow (Ctrl+C)
langflow run
```

Sometimes MCP servers get stuck and need a fresh start.

## 📝 Quick Reference Commands

```bash
# Activate environment
source venv/bin/activate

# Run Streamlit app
streamlit run streamlit_app.py

# Test simple request (no MCP)
python test_simple_request.py

# Check Playwright installation
python check_langflow_playwright.py

# Install Playwright (if needed)
bash install_playwright_server.sh
```

## 🎯 Summary

**Problem:** Always initializing MCP tools, even for simple messages  
**Solution:** Use Simplified Mode toggle to skip MCP when not needed  
**Result:** 5-10 second responses for simple chat! ⚡

