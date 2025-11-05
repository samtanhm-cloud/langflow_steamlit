import streamlit as st
import requests
import os
import uuid
import json
from mcp_tools_metadata import MCP_TOOLS_METADATA

st.set_page_config(page_title="Langflow API Client", page_icon="🤖", layout="wide")

st.title("🤖 Langflow API Client with Playwright MCP")

# Secure API configuration using Streamlit secrets
# API key and endpoint will be stored in secrets, not in code
try:
    api_endpoint = st.secrets.get("LANGFLOW_API_ENDPOINT", "")
    api_key = st.secrets.get("LANGFLOW_API_KEY", "")
except Exception:
    api_endpoint = ""
    api_key = ""

# Allow override in sidebar for testing
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Use secrets if available, otherwise show input fields
    if not api_endpoint:
        api_endpoint = st.text_input(
            "API Endpoint", 
            value="http://localhost:7860/api/v1/run/3cc7c38d-7371-49b0-a741-f20e9e902c8b",
            help="Your Langflow API endpoint URL"
        )
    else:
        st.success("✅ API Endpoint loaded from secrets")
        api_endpoint = st.text_input("API Endpoint", value=api_endpoint, disabled=True)
    
    if not api_key:
        api_key = st.text_input(
            "API Key", 
            type="password",
            help="Your Langflow API key (if required)"
        )
    else:
        st.success("✅ API Key loaded from secrets")
        # Show first few characters for debugging
        if len(api_key) > 4:
            st.caption(f"Key starts with: {api_key[:4]}...")
    
    st.divider()
    
    # Simplified mode toggle
    simplified_mode = st.checkbox(
        "🚀 Simplified Mode (Faster)",
        value=False,
        help="Send a simpler request without all MCP tools configured - useful for testing"
    )

# Main content area
st.header("💬 Chat Interface")

# Input message
input_value = st.text_area(
    "Enter your message:",
    value="Hello",
    height=100,
    placeholder="Type your message here..."
)

# System prompt customization
with st.expander("🎯 Advanced Settings"):
    system_prompt = st.text_area(
        "System Prompt (Agent)",
        value="You are a helpful assistant that can use tools to answer questions and perform tasks.",
        height=100
    )
    
    prompt_template = st.text_area(
        "Prompt Template",
        value="Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh.",
        height=100
    )

# Build payload
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "ChatInput-5DIkl": {
            "input_value": input_value
        },
        "Prompt-Jl3Kt": {
            "template": prompt_template
        },
        "Agent-LbPwq": {
            "input_value": "",
            "system_prompt": system_prompt
        }
    }
}

# Only add MCP Tools if NOT in simplified mode
if not simplified_mode:
    payload["tweaks"]["MCPTools-CKcKC"] = {
        "mcp_server": {
            "name": "playwright_extension",
            "config": {
                "command": "npx",
                "args": ["@playwright/mcp@latest"]
            }
        },
        "tools_metadata": MCP_TOOLS_METADATA
    }

# Generate session ID
payload["session_id"] = str(uuid.uuid4())

# Send request button
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    send_button = st.button("🚀 Send Request", type="primary", use_container_width=True)

with col2:
    if st.button("🔄 Clear", use_container_width=True):
        st.rerun()

if send_button:
    if not api_endpoint:
        st.error("❌ Please provide an API endpoint!")
    else:
        with st.spinner("🔄 Sending request..."):
            try:
                # Prepare headers
                headers = {"Content-Type": "application/json"}
                if api_key:
                    # Try multiple authentication formats
                    headers["Authorization"] = f"Bearer {api_key}"
                    headers["x-api-key"] = api_key  # Alternative header format
                
                # Send API request with extended timeout for complex operations
                st.info("⏳ This may take several minutes for complex requests (up to 10 min)...")
                response = requests.post(
                    api_endpoint,
                    json=payload,
                    headers=headers,
                    timeout=600  # 10 minutes timeout
                )
                
                # Check for authentication errors
                if response.status_code == 403:
                    st.error("🔒 Authentication Required!")
                    st.warning("⚠️ The API returned a 403 Forbidden error.")
                    
                    try:
                        error_detail = response.json().get("detail", "")
                        st.code(error_detail)
                    except:
                        pass
                    
                    st.info("""
                    **How to fix:**
                    1. **Add an API key** in the sidebar (if you have one)
                    2. OR contact your Langflow admin for access
                    3. OR for dev environments, you may need to set `LANGFLOW_SKIP_AUTH_AUTO_LOGIN=true` on the server
                    """)
                    st.stop()
                
                # Display response
                st.success(f"✅ Response received! Status: {response.status_code}")
                
                # Create tabs for different views
                tab1, tab2, tab3 = st.tabs(["📄 Response", "🔍 Raw JSON", "📊 Request Details"])
                
                with tab1:
                    st.subheader("Response")
                    try:
                        response_json = response.json()
                        st.json(response_json)
                    except:
                        st.text(response.text)
                
                with tab2:
                    st.subheader("Raw Response")
                    st.code(response.text, language="json")
                
                with tab3:
                    st.subheader("Request Details")
                    st.write("**Endpoint:**", api_endpoint)
                    st.write("**Session ID:**", payload["session_id"])
                    st.write("**Status Code:**", response.status_code)
                    st.write("**Headers:**", dict(response.headers))
                    
                    with st.expander("View Sent Payload"):
                        st.json(payload)
                
            except requests.exceptions.Timeout:
                st.error("⏱️ Request timed out (>10 minutes)")
                st.warning("""
                **Possible reasons:**
                - The Langflow server is processing a very complex request
                - The server might be overloaded or stuck
                - Network connectivity issues
                
                **Try:**
                1. Simplify your request (shorter message, fewer tools)
                2. Use "Simplified Mode" in the sidebar
                3. Check if the Langflow server is running: `curl http://localhost:7860`
                4. Contact your Langflow admin if the issue persists
                """)
            except requests.exceptions.ConnectionError:
                st.error("🔌 Connection error. Please check if the API endpoint is accessible.")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error making API request: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")

# Display info about the app
with st.expander("ℹ️ About this app"):
    st.markdown("""
    ### Langflow API Client
    
    This app sends requests to your Langflow API with Playwright MCP tools configured.
    
    **Features:**
    - 🔐 Secure API key management via Streamlit secrets
    - 🎯 Customizable system prompts and settings
    - 🤖 Pre-configured Playwright browser automation tools
    - 📊 Detailed response visualization
    
    **Note:** The Playwright MCP tools require:
    - The Langflow server must be accessible from where you run this app
    - The server must have Node.js and Playwright installed
    - Browser binaries must be available on the server
    """)

# Footer
st.divider()
st.caption("🔒 Your API keys are stored securely using Streamlit secrets and never exposed in the code.")

