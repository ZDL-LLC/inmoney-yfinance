#!/bin/sh
# Copy yfinance_ai.py from lkcair/yfinance-ai, byte for byte. Run before a release.
# Usage: ./sync.sh [ref]   (default main)
set -e
curl -fsSL "https://raw.githubusercontent.com/lkcair/yfinance-ai/${1:-main}/yfinance_ai.py" -o yfinance_ai.py
grep -m1 '^version:' yfinance_ai.py
