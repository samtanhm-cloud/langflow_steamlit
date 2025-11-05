# Secrets Configuration Guide

## 📝 Overview

This guide helps you set up API keys and secrets for your Streamlit + Langflow application.

## 🔐 Important Security Notes

- ⚠️ **NEVER** commit `.streamlit/secrets.toml` to git
- ✅ This file is already in `.gitignore` (protected)
- ✅ Use `secrets.toml.template` for sharing config structure (no real keys)

## 📍 Files

| File | Purpose | Commit to Git? |
|------|---------|----------------|
| `.streamlit/secrets.toml` | Your actual API keys | ❌ NO |
| `secrets.toml.template` | Template with placeholders | ✅ YES |

## 🚀 Quick Setup

### Step 1: Verify secrets file exists

```bash
cd /Users/tansa/Desktop/langflow_streamlit
ls -la .streamlit/secrets.toml
```

If it doesn't exist, create it:
```bash
mkdir -p .streamlit
cp secrets.toml.template .streamlit/secrets.toml
```

### Step 2: Get your Gemini API Key

1. Go to: **https://makersuite.google.com/app/apikey**
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key (starts with something like `AIza...`)

### Step 3: Update the secrets file

Open `.streamlit/secrets.toml` and replace the placeholders:

```toml
# ========================================
# Langflow Configuration
# ========================================

# Your Langflow API endpoint URL
LANGFLOW_API_ENDPOINT = "http://localhost:7860/api/v1/run/3cc7c38d-7371-49b0-a741-f20e9e902c8b"

# Your Langflow API key (if your Langflow instance requires authentication)
LANGFLOW_API_KEY = "sk-D4VYDYOgz9W-sYETn8XLpyQVfnu6tJahkrl6_zUy7ks"

# ========================================
# Gemini API Configuration
# ========================================

# Replace with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX"  # <-- PUT YOUR KEY HERE

# Use the same key here
GOOGLE_API_KEY = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX"  # <-- PUT YOUR KEY HERE
```

## 🔧 Configuration for Different Environments

### Local Development

```toml
LANGFLOW_API_ENDPOINT = "http://localhost:7860/api/v1/run/3cc7c38d-7371-49b0-a741-f20e9e902c8b"
GEMINI_API_KEY = "your-actual-gemini-key"
```

### Remote Langflow Server

```toml
LANGFLOW_API_ENDPOINT = "https://your-server.com/api/v1/run/3cc7c38d-7371-49b0-a741-f20e9e902c8b"
LANGFLOW_API_KEY = "your-langflow-auth-key"  # If authentication is enabled
GEMINI_API_KEY = "your-actual-gemini-key"
```

### Streamlit Cloud Deployment

When deploying to Streamlit Cloud:

1. Go to your app settings on Streamlit Cloud
2. Navigate to "Secrets" section
3. Paste your secrets in TOML format:

```toml
LANGFLOW_API_ENDPOINT = "http://your-server:7860/api/v1/run/3cc7c38d-7371-49b0-a741-f20e9e902c8b"
GEMINI_API_KEY = "your-actual-gemini-key"
GOOGLE_API_KEY = "your-actual-gemini-key"
```

## 🧪 Testing Your Configuration

### Test 1: Check if secrets are loaded

```bash
cd /Users/tansa/Desktop/langflow_streamlit
source venv/bin/activate
python -c "
import streamlit as st
try:
    endpoint = st.secrets.get('LANGFLOW_API_ENDPOINT', '')
    gemini_key = st.secrets.get('GEMINI_API_KEY', '')
    print(f'✅ Endpoint: {endpoint[:50]}...')
    print(f'✅ Gemini key loaded: {bool(gemini_key)}')
except Exception as e:
    print(f'❌ Error: {e}')
"
```

### Test 2: Test Gemini API

```bash
cd /Users/tansa/Desktop/langflow_streamlit
source venv/bin/activate
python test_gemini_api.py
```

Expected output:
```
✅ SUCCESS!
Response: Hello, DNS is working!
```

### Test 3: Run Streamlit App

```bash
streamlit run streamlit_app.py
```

Check the sidebar - you should see:
- ✅ API Endpoint loaded from secrets
- ✅ API Key loaded from secrets (if configured)

## 🐛 Troubleshooting

### Issue: "KeyError: 'GEMINI_API_KEY'"

**Solution:** The secrets file isn't being read. Check:

1. File exists at correct location:
   ```bash
   ls -la .streamlit/secrets.toml
   ```

2. File has correct format (TOML syntax)

3. Restart Streamlit app after editing secrets

### Issue: "403 Forbidden" from Gemini API

**Solution:** API key is invalid or quota exceeded

1. Verify your key at: https://makersuite.google.com/app/apikey
2. Check API quotas and billing
3. Generate a new key if needed

### Issue: "Secrets not loading in Streamlit"

**Solution:** 

1. Make sure file is named exactly: `.streamlit/secrets.toml`
2. Check TOML syntax (use quotes for strings)
3. Restart Streamlit (Ctrl+C and run again)
4. Clear browser cache

### Issue: "Connection refused to Langflow"

**Solution:**

1. Make sure Langflow is running:
   ```bash
   curl http://localhost:7860
   ```

2. If not running, start it:
   ```bash
   bash fix_gemini_dns.sh
   ```

## 📋 Current Configuration

Your current `.streamlit/secrets.toml` has been updated with:

- ✅ **Langflow Endpoint:** `http://localhost:7860/api/v1/run/3cc7c38d-7371-49b0-a741-f20e9e902c8b`
- ✅ **Langflow API Key:** (kept existing key)
- ⚠️ **Gemini API Key:** Placeholder - **YOU NEED TO UPDATE THIS!**

## 🎯 Next Steps

1. **Get your Gemini API key** from https://makersuite.google.com/app/apikey
2. **Edit** `.streamlit/secrets.toml` and replace `YOUR_GEMINI_API_KEY_HERE`
3. **Test** with: `python test_gemini_api.py`
4. **Run** Streamlit: `streamlit run streamlit_app.py`

## 📝 API Key Formats

### Gemini API Key Format
```
AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXX
```
- Starts with `AIza`
- About 39 characters long

### Langflow API Key Format (if using auth)
```
sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```
- Starts with `sk-`
- Variable length

## 🔗 Useful Links

- **Gemini API Keys:** https://makersuite.google.com/app/apikey
- **Gemini API Docs:** https://ai.google.dev/docs
- **Streamlit Secrets:** https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management
- **Langflow Docs:** https://docs.langflow.org/

## ✅ Verification Checklist

- [ ] `.streamlit/secrets.toml` exists
- [ ] Gemini API key is added (not placeholder)
- [ ] Langflow endpoint is correct
- [ ] File is NOT committed to git
- [ ] `test_gemini_api.py` passes
- [ ] Streamlit app loads successfully
- [ ] Can send messages and get responses

---

**Remember:** Keep your API keys secret! Never share them or commit them to version control. 🔒

