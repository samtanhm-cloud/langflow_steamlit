#!/usr/bin/env python3
"""
Quick test script to verify Langflow API connection
"""
import requests
import uuid

# API Configuration
url = "http://localizacstudio.ads.autodesk.com:7860/api/v1/run/4b06762f-7329-454b-b4a0-fcd2dc702b55"

# Simple test payload
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "Hello - this is a connection test",
    "session_id": str(uuid.uuid4()),
    "tweaks": {}
}

headers = {"Content-Type": "application/json"}

print(f"🔍 Testing connection to: {url}")
print(f"📤 Sending test request...")

try:
    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=10
    )
    
    print(f"\n✅ SUCCESS!")
    print(f"📊 Status Code: {response.status_code}")
    print(f"📝 Response:")
    print(response.text[:500])  # First 500 characters
    
except requests.exceptions.Timeout:
    print("\n❌ ERROR: Request timed out (>10 seconds)")
    print("The server is taking too long to respond.")
    
except requests.exceptions.ConnectionError as e:
    print("\n❌ ERROR: Connection failed")
    print(f"Details: {e}")
    print("\nPossible causes:")
    print("- API server is down")
    print("- Wrong URL")
    print("- Network/firewall blocking the connection")
    
except Exception as e:
    print(f"\n❌ ERROR: {type(e).__name__}")
    print(f"Details: {e}")

print("\n" + "="*50)
print("Test complete!")

