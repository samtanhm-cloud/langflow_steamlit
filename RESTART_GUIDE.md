# Complete Restart Guide

## 🚨 When You Need This

If you're getting the error:
```
Invalid argument provided to Gemini: 400
* GenerateContentRequest.tools[0].function_declarations[5].parameters.properties[paths].items: missing field.
```

**Even though the code is fixed**, this means **Python is using cached modules**.

## ✅ **Quick Restart (Recommended)**

### For Streamlit:

```bash
cd /Users/tansa/Desktop/langflow_streamlit
bash restart_streamlit.sh
```

This script will:
1. Clear Python cache
2. Kill old Streamlit processes
3. Verify metadata is correct
4. Start fresh Streamlit instance

### For Langflow:

**Terminal 1 (Langflow):**
```bash
# Stop with Ctrl+C, then:
cd /Users/tansa/Desktop/langflow_streamlit
bash fix_gemini_dns.sh
```

---

## 📋 **Manual Restart (Step-by-Step)**

### Step 1: Stop Everything

**Terminal where Streamlit is running:**
```bash
Ctrl + C
```

**Terminal where Langflow is running:**
```bash
Ctrl + C
```

### Step 2: Clear Python Cache

```bash
cd /Users/tansa/Desktop/langflow_streamlit
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -name "*.pyc" -delete
```

### Step 3: Verify Metadata is Fixed

```bash
python3 -c "from mcp_tools_metadata import MCP_TOOLS_METADATA; print(f'✅ {len(MCP_TOOLS_METADATA)} tools loaded')"
```

**Expected output:** `✅ 21 tools loaded`

### Step 4: Restart Langflow

```bash
bash fix_gemini_dns.sh
```

Wait until you see: `You can now view your app in your browser.`

### Step 5: Restart Streamlit

**New terminal:**
```bash
cd /Users/tansa/Desktop/langflow_streamlit
source venv/bin/activate
streamlit run streamlit_app.py
```

### Step 6: Clear Browser Cache

In your browser:
- **Mac:** `Cmd + Shift + R`
- **Windows/Linux:** `Ctrl + Shift + R`

Or:
1. Close ALL `localhost:8501` tabs
2. Reopen the Streamlit URL

---

## 🧪 **Verify the Fix Worked**

### Test 1: Check Streamlit Loads

You should see in the terminal:
```
✅ Loaded 21 tools
```

### Test 2: Send a Simple Request

1. In Streamlit UI, **enable "🚀 Simplified Mode"**
2. Enter: "Hello"
3. Click "🚀 Send Request"
4. Should respond in 5-10 seconds ✅

### Test 3: Test Browser Automation

1. **Disable "🚀 Simplified Mode"**
2. Enter: "Navigate to https://example.com"
3. Click "🚀 Send Request"
4. **Expected:** ✅ Success, no 400 error
5. **If you get 400 error:** Repeat restart procedure

---

## 🔍 **Troubleshooting**

### Issue: Still Getting 400 Error

**Solution 1: Force Kill Python Processes**
```bash
pkill -9 python3
pkill -9 streamlit
# Then restart everything
```

**Solution 2: Delete All Cache**
```bash
cd /Users/tansa/Desktop/langflow_streamlit
rm -rf __pycache__ .streamlit/cache
find . -name "*.pyc" -delete
python3 -m py_compile mcp_tools_metadata.py
```

**Solution 3: Restart Computer**
Sometimes Python processes hang. A full restart ensures clean state.

### Issue: "ModuleNotFoundError"

**Solution:**
```bash
cd /Users/tansa/Desktop/langflow_streamlit
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: Streamlit Shows Old Config

**Solution:**
```bash
# Clear Streamlit cache
rm -rf ~/.streamlit/cache
# Close ALL browser tabs with localhost:8501
# Restart Streamlit
```

### Issue: Langflow Not Starting

**Solution:**
```bash
# Check if port is in use
lsof -ti:7860 | xargs kill -9
# Restart Langflow
bash fix_gemini_dns.sh
```

---

## ✅ **Success Indicators**

You'll know the fix worked when:

1. ✅ Terminal shows: `✅ Loaded 21 tools`
2. ✅ No 400 errors in Streamlit response
3. ✅ Browser automation commands work
4. ✅ Can see all 21 tools in request payload (View Sent Payload)

---

## 🎯 **Quick Commands Reference**

```bash
# Complete restart (recommended)
cd /Users/tansa/Desktop/langflow_streamlit
bash restart_streamlit.sh  # In Terminal 1
bash fix_gemini_dns.sh     # In Terminal 2

# Verify metadata
python3 -c "from mcp_tools_metadata import MCP_TOOLS_METADATA; print(len(MCP_TOOLS_METADATA))"

# Clear cache manually
find . -type d -name "__pycache__" -exec rm -rf {} +

# Kill processes
pkill -f streamlit
pkill -f langflow

# Check ports
lsof -ti:8501  # Streamlit
lsof -ti:7860  # Langflow
```

---

## 📝 **Why This Happens**

Python caches imported modules in memory and `__pycache__` directories. When you update `mcp_tools_metadata.py`, Python may continue using the old cached version until:

1. The Python process is restarted
2. The cache is manually cleared
3. The module is force-reloaded

**Always restart after code changes to modules!**

---

## 🎉 **After Successful Restart**

You should be able to:
- ✅ Send simple chat messages (Simplified Mode ON)
- ✅ Use browser automation (Simplified Mode OFF)
- ✅ Upload files with `browser_file_upload`
- ✅ Click with modifiers using `browser_click`
- ✅ Use all 21 browser tools without errors

**Happy automating! 🚀**

