# Fixing Gemini API DNS Resolution Error

## 🚨 The Error

```
Error building Component Agent:
Timeout of 600.0s exceeded, last exception: 503 DNS resolution failed 
for generativelanguage.googleapis.com:443: C-ares status is not
```

## 🔍 What's Wrong?

The Python **gRPC library** (used by Google's Gemini API client) is having trouble resolving DNS using the **C-ares** resolver. This is a known issue with gRPC in certain Python environments.

**Your network is fine** - the issue is with Python's DNS resolution library, not your internet connection.

## ✅ Solution 1: Restart Langflow with DNS Fix (RECOMMENDED)

### Step 1: Stop Current Langflow

Press `Ctrl+C` in the terminal where Langflow is running, or:

```bash
pkill -f "langflow run"
```

### Step 2: Start with DNS Fix

**Option A - Automatic (recommended):**
```bash
bash fix_gemini_dns.sh
```

**Option B - Manual:**
```bash
source fix_gemini_dns_env.sh
langflow run
```

### What This Does:
Sets `GRPC_DNS_RESOLVER=native` to use your system's DNS instead of the problematic C-ares library.

## ✅ Solution 2: Permanent Fix

Add these environment variables to your shell profile:

```bash
# Add to ~/.zshrc or ~/.bash_profile
export GRPC_DNS_RESOLVER=native
export GRPC_ENABLE_IPV6=0
```

Then reload:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```

## ✅ Solution 3: Check Gemini API Key

The DNS error sometimes masks an API key issue. Verify your Gemini API key is configured:

### In Langflow UI:
1. Go to http://localhost:7860
2. Open your flow
3. Find the Gemini/GoogleGenerativeAI component
4. Check if API key is set correctly

### Test your API key:
```bash
export GOOGLE_API_KEY="your-api-key-here"

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${GOOGLE_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Hello"}]}]}'
```

If you get an error about invalid API key → **that's the real issue**!

## ✅ Solution 4: Update Dependencies

Sometimes the issue is with outdated gRPC or Google libraries:

```bash
# In your Langflow environment
uv pip install --upgrade grpcio google-generativeai google-cloud-aiplatform
```

## ✅ Solution 5: Use REST API Instead of gRPC

If gRPC keeps causing issues, configure Langflow to use REST API:

In Langflow's Gemini component settings, add:
```python
transport="rest"
```

Or in code:
```python
import google.generativeai as genai
genai.configure(api_key="...", transport="rest")
```

## 🧪 Testing the Fix

After applying the fix, test with a simple message in your Streamlit app:

1. Enable "Simplified Mode" in sidebar
2. Send: "Hello, how are you?"
3. Should respond in 5-10 seconds

## 🔍 Debugging: Enable Verbose Logging

If still having issues, start Langflow with debug logging:

```bash
export GRPC_VERBOSITY=debug
export GRPC_TRACE=http,dns_resolver
langflow run
```

Watch the logs for DNS resolution details.

## 📋 Common Issues & Solutions

### Issue: "GRPC_DNS_RESOLVER not working"

**Solution:** Make sure to set the variable BEFORE starting Langflow:
```bash
export GRPC_DNS_RESOLVER=native
langflow run  # Must be in same shell session
```

### Issue: "Still getting DNS errors"

**Solution:** Check if you're behind a corporate proxy:
```bash
# Set proxy if needed
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
export NO_PROXY=localhost,127.0.0.1

langflow run
```

### Issue: "Works sometimes, fails other times"

**Solution:** IPv6 DNS might be intermittent. Disable it:
```bash
export GRPC_ENABLE_IPV6=0
langflow run
```

### Issue: "Invalid API key" error now shows

**Good!** The DNS error was masking the real issue. Get a valid Gemini API key:
1. Go to https://makersuite.google.com/app/apikey
2. Create a new API key
3. Add it to your Langflow Gemini component

## 🎯 Quick Fix Summary

**Fastest solution:**
```bash
# Stop Langflow
pkill -f "langflow run"

# Set DNS fix
export GRPC_DNS_RESOLVER=native

# Restart Langflow
langflow run
```

Then test your Streamlit app again!

## 📁 Created Files

1. **`fix_gemini_dns.sh`** - Automatic fix script
2. **`fix_gemini_dns_env.sh`** - Environment variables to source
3. **`GEMINI_DNS_FIX.md`** - This guide

## 🔗 Related Issues

- [gRPC DNS Resolution Issue](https://github.com/grpc/grpc/issues/22422)
- [Google Generative AI Python SDK Issues](https://github.com/google/generative-ai-python/issues)

## ✅ Verification

After fixing, you should see in Langflow logs:
```
✅ Using native DNS resolver
✅ Successfully connected to Gemini API
```

And no more "C-ares" errors! 🎉

