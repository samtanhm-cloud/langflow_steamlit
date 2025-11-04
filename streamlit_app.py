import streamlit as st
import requests
import uuid
import json

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
            value="http://localizacstudio.ads.autodesk.com:7860/api/v1/run/4b06762f-7329-454b-b4a0-fcd2dc702b55",
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
    
    st.divider()
    
    # Model configuration
    st.subheader("Model Settings")
    ollama_base_url = st.text_input("Ollama Base URL", value="http://localhost:11434/")
    model_name = st.text_input("Model Name", value="gpt-oss:120b")
    n_messages = st.number_input("Max Messages", value=100, min_value=1)

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
        "System Prompt",
        value="You are a helpful assistant that can use tools to answer questions and perform tasks.",
        height=100
    )
    
    format_instructions = st.text_area(
        "Format Instructions",
        value="You are an AI that extracts structured JSON objects from unstructured text. Use a predefined schema with expected types (str, int, float, bool, dict). Extract ALL relevant instances that match the schema - if multiple patterns exist, capture them all. Fill missing or ambiguous values with defaults: None for missing values. Remove exact duplicates but keep variations that have different field values. Always return valid JSON in the expected format, never throw errors. If multiple objects can be extracted, return them all in the structured format.",
        height=150
    )

# Build payload
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": input_value,
    "tweaks": {
        "Agent-9hWQI": {
            "format_instructions": format_instructions,
            "n_messages": n_messages,
            "output_schema": [],
            "system_prompt": system_prompt
        },
        "OllamaModel-F13V6": {
            "base_url": ollama_base_url,
            "model_name": model_name
        },
        "MCPTools-qmP5R": {
            "mcp_server": {
                "name": "playwright_extension",
                "config": {
                    "command": "npx",
                    "args": ["@playwright/mcp@latest"]
                }
            },
            "tools_metadata": [
                {
                    "name": "browser_close",
                    "description": "Close the page",
                    "tags": ["browser_close"],
                    "status": True,
                    "display_name": "browser_close",
                    "display_description": "Close the page",
                    "readonly": False,
                    "args": {}
                },
                {
                    "name": "browser_resize",
                    "description": "Resize the browser window",
                    "tags": ["browser_resize"],
                    "status": True,
                    "display_name": "browser_resize",
                    "display_description": "Resize the browser window",
                    "readonly": False,
                    "args": {
                        "width": {
                            "description": "Width of the browser window",
                            "title": "Width",
                            "type": "number"
                        },
                        "height": {
                            "description": "Height of the browser window",
                            "title": "Height",
                            "type": "number"
                        }
                    }
                },
                {
                    "name": "browser_console_messages",
                    "description": "Returns all console messages",
                    "tags": ["browser_console_messages"],
                    "status": True,
                    "display_name": "browser_console_messages",
                    "display_description": "Returns all console messages",
                    "readonly": False,
                    "args": {
                        "onlyErrors": {
                            "anyOf": [
                                {"type": "boolean"},
                                {"type": "None"}
                            ],
                            "default": None,
                            "description": "Only return error messages",
                            "title": "Onlyerrors"
                        }
                    }
                },
                {
                    "name": "browser_navigate",
                    "description": "Navigate to a URL",
                    "tags": ["browser_navigate"],
                    "status": True,
                    "display_name": "browser_navigate",
                    "display_description": "Navigate to a URL",
                    "readonly": False,
                    "args": {
                        "url": {
                            "description": "The URL to navigate to",
                            "title": "Url",
                            "type": "string"
                        }
                    }
                },
                {
                    "name": "browser_snapshot",
                    "description": "Capture accessibility snapshot of the current page",
                    "tags": ["browser_snapshot"],
                    "status": True,
                    "display_name": "browser_snapshot",
                    "display_description": "Capture accessibility snapshot of the current page",
                    "readonly": False,
                    "args": {}
                },
                {
                    "name": "browser_click",
                    "description": "Perform click on a web page",
                    "tags": ["browser_click"],
                    "status": True,
                    "display_name": "browser_click",
                    "display_description": "Perform click on a web page",
                    "readonly": False,
                    "args": {
                        "element": {
                            "description": "Human-readable element description",
                            "title": "Element",
                            "type": "string"
                        },
                        "ref": {
                            "description": "Exact target element reference",
                            "title": "Ref",
                            "type": "string"
                        }
                    }
                }
            ]
        }
    }
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
                    headers["Authorization"] = f"Bearer {api_key}"
                
                # Send API request
                response = requests.post(
                    api_endpoint,
                    json=payload,
                    headers=headers,
                    timeout=30
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
                st.error("⏱️ Request timed out. The server took too long to respond.")
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

