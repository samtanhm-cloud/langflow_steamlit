#!/usr/bin/env python3
"""
Simple test script to send a request WITHOUT MCP tools
This should respond in 5-10 seconds with Gemini
"""

import requests
import json
import uuid

# Configuration
LANGFLOW_API = "http://localhost:7860/api/v1/run/4b06762f-7329-454b-b4a0-fcd2dc702b55"

# Minimal payload without MCP tools
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Hello! Please respond with 'Hi there!'",
    "session_id": str(uuid.uuid4())
}

print("🚀 Sending simple test request (no MCP tools)...")
print(f"Message: {payload['input_value']}")
print("⏱️  Starting timer...")

try:
    response = requests.post(
        LANGFLOW_API,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=30  # Should respond within 30 seconds
    )
    
    print(f"\n✅ Response received!")
    print(f"Status: {response.status_code}")
    print(f"\nResponse:")
    print(json.dumps(response.json(), indent=2))
    
except requests.exceptions.Timeout:
    print("\n❌ Request timed out (>30 seconds)")
    print("Something is wrong with the Langflow server or Gemini API")
    
except Exception as e:
    print(f"\n❌ Error: {e}")

