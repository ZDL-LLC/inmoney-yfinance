# yfinance-ai MCP server

<!-- mcp-name: io.github.lkcair/yfinance-ai -->

Yahoo Finance for any MCP client in **68 tools**: real-time quotes, history, fundamentals, analyst ratings and estimates, options, holders and insiders, dividends, funds and ETFs, crypto, forex, commodities, market movers, sectors and earnings, IPO and economic calendars. No API key.

Powered by [yfinance-ai](https://github.com/lkcair/yfinance-ai), our Yahoo Finance toolkit with thousands of downloads on ClawHub and OpenWebUI.

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
