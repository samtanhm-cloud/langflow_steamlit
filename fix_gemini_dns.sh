#!/bin/bash
# Fix for Gemini API DNS resolution issues
# This forces Python/gRPC to use the system DNS resolver instead of C-ares

echo "🔧 Applying DNS resolution fix for Gemini API..."
echo ""

# Set environment variables to fix gRPC DNS resolution
export GRPC_DNS_RESOLVER=native
export GRPC_VERBOSITY=debug
export GRPC_TRACE=http

echo "✅ Set environment variables:"
echo "   GRPC_DNS_RESOLVER=native (use system DNS instead of C-ares)"
echo ""

# Also try alternative DNS resolvers
export USE_SYSTEM_DNS=1
export GRPC_ENABLE_FORK_SUPPORT=0

echo "🚀 Starting Langflow with fixed DNS settings..."
echo ""

# Stop existing Langflow (if running)
pkill -f "langflow run" 2>/dev/null || true
sleep 2

# Start Langflow with proper DNS configuration
echo "Starting: uv run langflow run"
echo ""
uv run langflow run

