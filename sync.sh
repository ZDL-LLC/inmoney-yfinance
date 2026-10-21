#!/bin/sh
# Copy yfinance_ai.py from lkcair/yfinance-ai, byte for byte. Run before a release.
# Usage: ./sync.sh [ref]   (default main)
set -e
# Resolve the ref to a commit first: raw files by branch name can be minutes stale after a push
sha="$(git ls-remote https://github.com/lkcair/yfinance-ai.git "${1:-main}" | cut -f1 | head -1)"
[ -n "$sha" ] || sha="${1:-main}"   # a commit id given directly
curl -fsSL "https://raw.githubusercontent.com/lkcair/yfinance-ai/$sha/yfinance_ai.py" -o yfinance_ai.py
grep -m1 '^version:' yfinance_ai.py
