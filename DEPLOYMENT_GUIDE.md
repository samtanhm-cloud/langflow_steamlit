# 🚀 Streamlit Cloud Deployment Guide

## Step-by-Step Instructions

### 1️⃣ Prepare Your Repository

1. **Create a new GitHub repository**
   - Go to https://github.com/new
   - Name it (e.g., `langflow-streamlit-app`)
   - Make it **Private** (recommended for security)
   - Don't add README, .gitignore, or license (we have them)

2. **Upload these files to your repository:**
   ```
   streamlit_app.py          ← Main app file
   requirements.txt          ← Python dependencies
   .gitignore               ← Protects secrets
   secrets.toml.template    ← Template for secrets (safe to commit)
   DEPLOYMENT_GUIDE.md      ← This guide
   ```

3. **Initialize and push to GitHub:**
   ```bash
   cd /Users/tansa/Downloads
   git init
   git add streamlit_app.py requirements.txt .gitignore secrets.toml.template DEPLOYMENT_GUIDE.md
   git commit -m "Initial commit: Langflow API Streamlit app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

   **⚠️ IMPORTANT:** Make sure you DON'T commit any file with actual API keys!

---

### 2️⃣ Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Create a new app**
   - Click "New app"
   - Select your repository
   - Branch: `main`
   - Main file path: `streamlit_app.py`
   - Click "Deploy"

---

### 3️⃣ Add Your Secrets to Streamlit Cloud

**This is where you securely add your API key!**

1. **In Streamlit Cloud dashboard:**
   - Click on your app
   - Click the "⚙️" (settings) icon
   - Go to "Secrets" section

2. **Add your secrets in TOML format:**
   ```toml
   LANGFLOW_API_ENDPOINT = "http://localizacstudio.ads.autodesk.com:7860/api/v1/run/4b06762f-7329-454b-b4a0-fcd2dc702b55"
   LANGFLOW_API_KEY = "your-actual-api-key-here"
   ```

3. **Click "Save"**
   - Your app will automatically restart with the secrets

---

### 4️⃣ For Local Development

If you want to test locally before deploying:

1. **Create a secrets directory:**
   ```bash
   mkdir -p .streamlit
   ```

2. **Create the secrets file:**
   ```bash
   cp secrets.toml.template .streamlit/secrets.toml
   ```

3. **Edit `.streamlit/secrets.toml` with your actual values:**
   ```toml
   LANGFLOW_API_ENDPOINT = "your-endpoint"
   LANGFLOW_API_KEY = "your-key"
   ```

4. **Run locally:**
   ```bash
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```

---

## ⚠️ Security Best Practices

### ✅ DO:
- ✅ Store API keys in Streamlit Cloud secrets
- ✅ Add `.streamlit/secrets.toml` to `.gitignore`
- ✅ Use private repositories for sensitive projects
- ✅ Only commit the `secrets.toml.template` file
- ✅ Regularly rotate your API keys

### ❌ DON'T:
- ❌ Never hardcode API keys in your code
- ❌ Never commit `.streamlit/secrets.toml` to git
- ❌ Never share your secrets.toml file
- ❌ Never push files with actual API keys to public repos

---

## 🔧 Important Notes

### Network Access
Your Streamlit Cloud app may not be able to access:
- `http://localizacstudio.ads.autodesk.com:7860` (internal Autodesk network)
- `http://localhost:11434/` (local Ollama instance)

**Solutions:**
1. **Use a publicly accessible API endpoint**
2. **Set up a VPN or tunnel** (e.g., ngrok, CloudFlare Tunnel)
3. **Deploy on a server within your network** instead of Streamlit Cloud

### Playwright MCP Requirements
The Playwright browser automation tools require:
- Node.js installed on the server
- Browser binaries (Chromium, Firefox, or WebKit)
- These may not work on Streamlit Cloud's restricted environment

**Alternative:** Consider using a different deployment platform like:
- **AWS EC2** or **GCP Compute Engine** (full control)
- **Railway.app** (easier than cloud VMs)
- **Docker** on your own infrastructure

---

## 🆘 Troubleshooting

### Error: "Connection refused"
- Your API endpoint is not accessible from Streamlit Cloud
- Use a publicly accessible URL or set up a tunnel

### Error: "API key invalid"
- Check that you've added secrets correctly in Streamlit Cloud
- Verify the key format matches what your API expects

### App won't deploy
- Check that `requirements.txt` is present
- Verify Python package versions are compatible
- Check Streamlit Cloud logs for specific errors

---

## 📚 Additional Resources

- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [GitHub Guide](https://docs.github.com/en/get-started/quickstart)

---

## 🎯 Quick Start Checklist

- [ ] Create GitHub repository
- [ ] Upload all necessary files (except secrets!)
- [ ] Push to GitHub
- [ ] Deploy on Streamlit Cloud
- [ ] Add secrets in Streamlit Cloud settings
- [ ] Test the app
- [ ] Verify API connectivity

Good luck! 🚀

