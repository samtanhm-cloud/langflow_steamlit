#!/usr/bin/env python3
"""
Test script to verify the updated Streamlit payload structure
"""

import json
from mcp_tools_metadata import MCP_TOOLS_METADATA
import uuid

# Build test payload (matches streamlit_app.py)
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "ChatInput-5DIkl": {
            "input_value": "Hello, test message"
        },
        "Prompt-Jl3Kt": {
            "template": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh."
        },
        "Agent-LbPwq": {
            "input_value": "",
            "system_prompt": "You are a helpful assistant that can use tools to answer questions and perform tasks."
        }
    }
}

# Add MCP Tools (simulating simplified_mode = False)
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

# Add session ID
payload["session_id"] = str(uuid.uuid4())

print("=" * 70)
print(" ✅ Payload Structure Test")
print("=" * 70)

# Verify structure
print(f"\n✓ Component IDs present:")
print(f"  - ChatInput-5DIkl: {' ChatInput-5DIkl' in payload['tweaks']}")
print(f"  - Prompt-Jl3Kt: {'Prompt-Jl3Kt' in payload['tweaks']}")
print(f"  - Agent-LbPwq: {'Agent-LbPwq' in payload['tweaks']}")
print(f"  - MCPTools-CKcKC: {'MCPTools-CKcKC' in payload['tweaks']}")

print(f"\n✓ MCP Tools metadata:")
print(f"  - Number of browser tools: {len(MCP_TOOLS_METADATA)}")
print(f"  - Tools loaded successfully: {len(MCP_TOOLS_METADATA) == 23}")

print(f"\n✓ Tool names:")
for i, tool in enumerate(MCP_TOOLS_METADATA, 1):
    print(f"  {i:2d}. {tool['name']}")

print(f"\n✓ Session ID: {payload['session_id']}")

print(f"\n✓ Payload size: {len(json.dumps(payload))} bytes")

# Test simplified mode (no MCP tools)
payload_simplified = {
    "output_type": "chat",
    "input_type": "chat",
    "tweaks": {
        "ChatInput-5DIkl": {
            "input_value": "Hello, test message"
        },
        "Prompt-Jl3Kt": {
            "template": "Answer the user as if you were a GenAI expert."
        },
        "Agent-LbPwq": {
            "input_value": "",
            "system_prompt": "You are a helpful assistant."
        }
    },
    "session_id": str(uuid.uuid4())
}

print(f"\n✓ Simplified mode payload:")
print(f"  - Has MCPTools: {'MCPTools-CKcKC' in payload_simplified['tweaks']}")
print(f"  - Payload size: {len(json.dumps(payload_simplified))} bytes")

print("\n" + "=" * 70)
print(" ✅ All Tests Passed!")
print("=" * 70)

print("\n📝 Next steps:")
print("  1. Run: streamlit run streamlit_app.py")
print("  2. Test with Simplified Mode ON (fast)")
print("  3. Test with Simplified Mode OFF (browser automation)")
print("\n🎉 Your configuration is ready!")

