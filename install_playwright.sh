#!/bin/bash
# Script to install Playwright browsers
# This script should be run after installing the Python packages

echo "Installing Playwright browsers..."
playwright install chromium
playwright install-deps chromium

echo "Playwright Chromium installation complete!"

