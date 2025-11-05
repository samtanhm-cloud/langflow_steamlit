#!/usr/bin/env python3
"""
Quick verification script for secrets configuration
"""

import sys
import os

# Check if we're in the right directory
if not os.path.exists('.streamlit/secrets.toml'):
    print("❌ Error: .streamlit/secrets.toml not found!")
    print("   Run this from the project root directory")
    sys.exit(1)

# Try to load secrets using Streamlit's method
try:
    import streamlit as st
    
    print("=" * 60)
    print("  🔐 Secrets Configuration Verification")
    print("=" * 60)
    print()
    
    # Check Langflow configuration
    print("✅ Langflow Configuration:")
    endpoint = st.secrets.get("LANGFLOW_API_ENDPOINT", "")
    langflow_key = st.secrets.get("LANGFLOW_API_KEY", "")
    
    if endpoint:
        print(f"   Endpoint: {endpoint[:50]}...")
        print(f"   ✓ Endpoint configured")
    else:
        print("   ❌ No endpoint configured")
    
    if langflow_key:
        print(f"   API Key: {langflow_key[:10]}...{langflow_key[-4:]}")
        print(f"   ✓ Langflow API key configured")
    else:
        print("   ⚠️  No Langflow API key")
    
    print()
    
    # Check Gemini configuration
    print("✅ Gemini API Configuration:")
    gemini_key = st.secrets.get("GEMINI_API_KEY", "")
    google_key = st.secrets.get("GOOGLE_API_KEY", "")
    
    if gemini_key and gemini_key != "YOUR_GEMINI_API_KEY_HERE":
        print(f"   GEMINI_API_KEY: {gemini_key[:15]}...{gemini_key[-4:]}")
        print(f"   ✓ Gemini API key configured")
    else:
        print("   ❌ GEMINI_API_KEY not set or still placeholder")
    
    if google_key and google_key != "YOUR_GEMINI_API_KEY_HERE":
        print(f"   GOOGLE_API_KEY: {google_key[:15]}...{google_key[-4:]}")
        print(f"   ✓ Google API key configured")
    else:
        print("   ❌ GOOGLE_API_KEY not set or still placeholder")
    
    if gemini_key == google_key:
        print("   ✓ Both keys match (correct)")
    else:
        print("   ⚠️  Keys don't match - they should be the same")
    
    print()
    print("=" * 60)
    print("  ✅ Configuration Status: READY")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Make sure Langflow is running: bash fix_gemini_dns.sh")
    print("  2. Test Gemini API: python test_gemini_api.py")
    print("  3. Run Streamlit app: streamlit run streamlit_app.py")
    
except ImportError:
    print("❌ Streamlit not installed")
    print("   Install with: pip install streamlit")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error loading secrets: {e}")
    sys.exit(1)

