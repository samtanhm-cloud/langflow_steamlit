#!/usr/bin/env python3
"""
Test Gemini API connectivity and API key validity
This helps diagnose if the issue is DNS or API key related
"""

import os
import sys

# Try to import required libraries
try:
    import google.generativeai as genai
    print("✅ google-generativeai library is installed")
except ImportError:
    print("❌ google-generativeai library not found!")
    print("   Install with: pip install google-generativeai")
    sys.exit(1)

# Check for API key
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⚠️  No API key found in environment!")
    print("")
    print("Please set your Gemini API key:")
    print("  export GOOGLE_API_KEY='your-key-here'")
    print("")
    print("Or get one from: https://makersuite.google.com/app/apikey")
    print("")
    api_key = input("Enter your Gemini API key (or press Enter to skip): ").strip()
    if not api_key:
        print("Skipping API test.")
        sys.exit(0)

print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")
print("")

# Configure with different transport options
print("=" * 60)
print("Test 1: Using gRPC transport (default)")
print("=" * 60)

try:
    # Set DNS resolver to native
    os.environ["GRPC_DNS_RESOLVER"] = "native"
    os.environ["GRPC_ENABLE_IPV6"] = "0"
    
    print("Setting GRPC_DNS_RESOLVER=native")
    
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say 'Hello, DNS is working!'")
    
    print("✅ SUCCESS!")
    print(f"Response: {response.text}")
    print("")
    
except Exception as e:
    print(f"❌ gRPC transport failed: {e}")
    print("")
    
    # Try REST transport as fallback
    print("=" * 60)
    print("Test 2: Trying REST transport (fallback)")
    print("=" * 60)
    
    try:
        genai.configure(api_key=api_key, transport="rest")
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Say 'Hello, REST API is working!'")
        
        print("✅ SUCCESS with REST!")
        print(f"Response: {response.text}")
        print("")
        print("💡 Recommendation: Configure Langflow to use REST transport")
        
    except Exception as e2:
        print(f"❌ REST transport also failed: {e2}")
        print("")
        print("Possible issues:")
        print("1. Invalid API key")
        print("2. Network/firewall blocking Google APIs")
        print("3. API quota exceeded")
        print("")

print("=" * 60)
print("Summary")
print("=" * 60)
print("")
print("If gRPC worked:")
print("  → Restart Langflow with: export GRPC_DNS_RESOLVER=native")
print("")
print("If only REST worked:")
print("  → Configure Langflow Gemini component to use REST transport")
print("")
print("If both failed:")
print("  → Check your API key at https://makersuite.google.com/app/apikey")
print("  → Verify network access to Google APIs")

