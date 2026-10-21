# yfinance-ai MCP server

<!-- mcp-name: io.github.lkcair/yfinance-ai -->

Yahoo Finance for any MCP client in **68 tools**: real-time quotes, history, fundamentals, analyst ratings and estimates, options, holders and insiders, dividends, funds and ETFs, crypto, forex, commodities, market movers, sectors and earnings, IPO and economic calendars. No API key.

The tools are [yfinance-ai](https://github.com/lkcair/yfinance-ai), the same file used by thousands on ClawHub and OpenWebUI. This package serves them over MCP.

## Install

**Claude Code**
```bash
claude mcp add yfinance-ai -- uvx yfinance-ai
```

**Claude Desktop, Cursor, VS Code and other clients**
```json
{
  "mcpServers": {
    "yfinance-ai": { "command": "uvx", "args": ["yfinance-ai"] }
  }
}
```

Without [uv](https://docs.astral.sh/uv/): `pip install yfinance-ai` and use `"command": "yfinance-ai"`.

## Try

- "Compare AAPL, MSFT and GOOGL on valuation"
- "What are analysts saying about NVIDIA?"
- "Top gainers today" / "Who reports earnings this week?"
- "Bitcoin price" / "EUR/USD rate" / "SPY top holdings"

Every tool is read-only. Full tool list: [yfinance-ai README](https://github.com/lkcair/yfinance-ai#%EF%B8%8F-available-tools-68).

MIT. Data comes from Yahoo Finance through [yfinance](https://github.com/ranaroussi/yfinance) and may be delayed. Not affiliated with Yahoo. For research and education, not investment advice.

## How it is built

`yfinance_ai.py` is an exact copy of the file in [lkcair/yfinance-ai](https://github.com/lkcair/yfinance-ai/blob/main/yfinance_ai.py), the same file OpenWebUI and ClawHub use. `yfinance_ai_mcp.py` imports it and registers every tool over MCP. The package version is read from the `.py` header.

## Release

After a new version is on `main` in [lkcair/yfinance-ai](https://github.com/lkcair/yfinance-ai):

```bash
./sync.sh                               # copy yfinance_ai.py from its repo
git commit -am "yfinance-ai X.Y.Z" && git push
git tag vX.Y.Z && git push --tags       # publish.yml: PyPI + MCP Registry
```

The workflow refuses to publish if the copy differs from its repo or the tag differs from the `.py` version.
