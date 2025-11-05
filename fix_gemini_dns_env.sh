#!/bin/bash
# Environment variables to fix Gemini DNS issues
# Source this file before running Langflow: source fix_gemini_dns_env.sh

# Force gRPC to use system DNS resolver instead of C-ares
export GRPC_DNS_RESOLVER=native

# Alternative: use ares resolver with specific settings
# export GRPC_DNS_RESOLVER=ares

# Enable IPv4 only (sometimes helps with DNS issues)
export GRPC_ENABLE_IPV6=0

# Use system DNS configuration
export USE_SYSTEM_DNS=1

# Disable fork support (can cause DNS issues in some environments)
export GRPC_ENABLE_FORK_SUPPORT=0

# Optional: Enable debug logging to see DNS resolution details
# export GRPC_VERBOSITY=debug
# export GRPC_TRACE=http,dns_resolver

echo "✅ DNS fix environment variables set!"
echo "   GRPC_DNS_RESOLVER=native"
echo "   GRPC_ENABLE_IPV6=0"
echo ""
echo "Now run: langflow run"

