# 🤖 Langflow API Streamlit App

A Streamlit web application for interacting with Langflow API with Playwright MCP browser automation tools.

## 🚀 Quick Start

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions on deploying to Streamlit Cloud.

## 📁 Files

- `streamlit_app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies
- `secrets.toml.template` - Template for secrets configuration
- `.gitignore` - Protects sensitive files from being committed
- `DEPLOYMENT_GUIDE.md` - Step-by-step deployment instructions

## 🔐 Security

**Never commit your actual API keys!** 

- Use Streamlit Cloud secrets for production
- Use `.streamlit/secrets.toml` for local development (this file is gitignored)

## 💻 Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create secrets file:
   ```bash
   mkdir -p .streamlit
   cp secrets.toml.template .streamlit/secrets.toml
   ```

3. Edit `.streamlit/secrets.toml` with your actual values

4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## ☁️ Deploy to Streamlit Cloud

1. Push this code to GitHub
2. Go to https://share.streamlit.io/
3. Deploy your app
4. Add secrets in the Streamlit Cloud dashboard

**See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete instructions.**

## ⚠️ Important Notes

- Your API endpoint must be publicly accessible for Streamlit Cloud deployment
- Internal network URLs (like `localizacstudio.ads.autodesk.com`) won't work from Streamlit Cloud
- Consider using a VPN/tunnel or deploying on your own infrastructure if you need access to internal networks

## 📝 License

Your license here.

