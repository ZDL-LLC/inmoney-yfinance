# yfinance-ai MCP server

<!-- mcp-name: io.github.lkcair/yfinance-ai -->

[![PyPI](https://img.shields.io/pypi/v/yfinance-ai)](https://pypi.org/project/yfinance-ai/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

World's first AI-powered Yahoo Finance integration: 68 tools for stocks, ETFs, mutual funds, crypto, forex and commodities, in one Python file.

🚀 **Thousands of downloads on ClawHub and OpenWebUI**

Prices and history, financial statements, ratios and valuation history, analyst estimates and price targets, earnings, dividends, options, holders and insiders, funds and ETFs, market movers, sectors and industries, and earnings, IPO, economic and split calendars.

| Use it in | Install | Repo |
|---|---|---|
| Claude, Cursor, VS Code, [LangChain](https://docs.langchain.com/oss/python/langchain/mcp), [Google ADK](https://google.github.io/adk-docs/tools-custom/mcp-tools/), [Strands Agents](https://strandsagents.com/docs/user-guide/sdk/tools/mcp-tools/) and other MCP clients | `uvx yfinance-ai@latest` | [yfinance-ai-mcp](https://github.com/lkcair/yfinance-ai-mcp) |
| ClawHub skill for OpenClaw 🚀 Thousands of downloads | `openclaw skills install @lkcair/stocks` | [yfinance-ai-skill](https://github.com/lkcair/yfinance-ai-skill) |
| OpenWebUI tool 🚀 Thousands of downloads | [Get it on openwebui.com](https://openwebui.com/posts/finance_data_pull_ai_tool_yahoo_finance_yfinance_fc928bb1) | [yfinance-ai](https://github.com/lkcair/yfinance-ai) |
| Python | `from yfinance_ai import Tools` | [yfinance-ai](https://github.com/lkcair/yfinance-ai) |


## Install

Needs [uv](https://docs.astral.sh/uv/getting-started/installation/). No API key.

Claude Code:
```bash
claude mcp add yfinance-ai -- uvx yfinance-ai@latest
```

VS Code:
```bash
code --add-mcp '{"name":"yfinance-ai","type":"stdio","command":"uvx","args":["yfinance-ai@latest"]}'
```

Claude Desktop, Cursor, Windsurf and other clients, in the client's MCP config file:
```json
{
  "mcpServers": {
    "yfinance-ai": {
      "command": "uvx",
      "args": [
        "yfinance-ai@latest"
      ]
    }
  }
}
```

`@latest` picks up new releases when the client starts. Without uv: `pip install yfinance-ai`, then use `"command": "yfinance-ai"` with no args.

Listed in the [MCP Registry](https://registry.modelcontextprotocol.io) as `io.github.lkcair/yfinance-ai`. Every tool is read-only.

## Agent frameworks

The server runs over stdio with `uvx yfinance-ai@latest`, so any framework with MCP support can load all its tools.

[LangChain](https://docs.langchain.com/oss/python/langchain/mcp): `pip install "langchain[mcp]" langchain-anthropic`
```python
import asyncio
from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

async def main():
    config = {"mcpServers": {"yfinance-ai": {
        "command": "uvx", "args": ["yfinance-ai@latest"],
    }}}
    async with MCPAdapter(config) as adapter:
        tools = await adapter.list_tools()
        agent = create_agent("claude-sonnet-5", tools)
        result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is Apple's P/E, and how does it compare with Microsoft and Google?"}]})
        print(result["messages"][-1].content)

asyncio.run(main())
```

[Google ADK](https://google.github.io/adk-docs/tools-custom/mcp-tools/): `pip install "google-adk[mcp]"`
```python
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

root_agent = LlmAgent(
    model="gemini-flash-latest",
    name="yfinance_ai",
    instruction="Answer with the yfinance-ai tools.",
    tools=[McpToolset(connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(command="uvx", args=["yfinance-ai@latest"]),
        timeout=60,
    ))],
)
```

[Strands Agents](https://strandsagents.com/docs/user-guide/sdk/tools/mcp-tools/): `pip install strands-agents`
```python
from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient

yfinance_ai = MCPClient(lambda: stdio_client(StdioServerParameters(
    command="uvx", args=["yfinance-ai@latest"],
)))
agent = Agent(tools=[yfinance_ai])
agent("What is Apple's P/E, and how does it compare with Microsoft and Google?")
```

## Example questions

- What is Apple's P/E, and how does it compare with Microsoft and Google?
- What are analysts saying about NVIDIA? Price targets and recent upgrades.
- Who reports earnings this week?
- Bitcoin price, EUR/USD rate and gold today.

## MCP tools (68)

### Quotes and history

| Tool | Parameters | Description |
|---|---|---|
| `get_stock_price` | `ticker` | Get current stock price and key metrics for a ticker symbol |
| `get_stock_quote` | `ticker` | Get detailed quote with bid/ask, day range, and trading info |
| `get_fast_info` | `ticker` | Get fast-access ticker information (lightweight, quick response) |
| `get_historical_data` | `ticker, period="1y", interval="1d"` | Get historical price data for a stock |
| `get_historical_price_on_date` | `ticker, date` | Get historical price for a specific date |
| `download_multiple_tickers` | `tickers, period="1mo", interval="1d"` | Historical data for several tickers at once |

### Company

| Tool | Parameters | Description |
|---|---|---|
| `get_company_info` | `ticker` | Get detailed company information and business description |
| `get_company_overview` | `ticker` | Company overview with context for every metric |
| `get_company_officers` | `ticker` | Get company officers and key management |
| `get_isin` | `ticker` | Get International Securities Identification Number (ISIN) for a ticker |

### Financials

| Tool | Parameters | Description |
|---|---|---|
| `get_income_statement` | `ticker, period="annual"` | Get income statement data |
| `get_balance_sheet` | `ticker, period="annual"` | Get balance sheet data |
| `get_cash_flow` | `ticker, period="annual"` | Get cash flow statement data |
| `get_ttm_financials` | `ticker` | Get trailing-twelve-month (TTM) income statement and cash flow |
| `get_key_ratios` | `ticker` | Get key financial ratios and valuation metrics |
| `get_valuation_history` | `ticker` | Get valuation measures now and for the last quarters (market cap, EV, P/E, PEG, P/S, P/B, EV/EBITDA) |
| `get_financial_summary` | `ticker` | Get a comprehensive one-page financial summary of a stock |
| `get_shares_history` | `ticker, years=3` | Get shares outstanding over time (dilution or buybacks) |

### Earnings and estimates

| Tool | Parameters | Description |
|---|---|---|
| `get_earnings_dates` | `ticker` | Get upcoming and past earnings dates with estimates |
| `get_earnings_history` | `ticker` | Get historical earnings data with annual and quarterly figures |
| `get_earnings_calendar` | `ticker` | Get earnings calendar including next earnings date and dividend dates |
| `get_analyst_estimates` | `ticker` | Get analyst estimates for earnings, revenue, and EPS |
| `get_growth_estimates` | `ticker` | Get analyst growth estimates |
| `get_eps_trend` | `ticker` | Get EPS (Earnings Per Share) trend data showing how estimates have changed |
| `get_eps_revisions` | `ticker` | Get EPS revision data showing analyst estimate changes |

### Analysts

| Tool | Parameters | Description |
|---|---|---|
| `get_analyst_recommendations` | `ticker` | Get analyst recommendations and ratings |
| `get_analyst_price_targets` | `ticker` | Get detailed analyst price targets for a stock |
| `get_upgrades_downgrades` | `ticker, limit=20` | Get detailed analyst upgrades and downgrades history |

### Holders and insiders

| Tool | Parameters | Description |
|---|---|---|
| `get_institutional_holders` | `ticker` | Get major institutional holders and their ownership |
| `get_major_holders` | `ticker` | Get major holders summary (institutions, insiders, public float) |
| `get_mutualfund_holders` | `ticker` | Get mutual fund holders |
| `get_insider_transactions` | `ticker` | Get recent insider trading activity |
| `get_insider_purchases` | `ticker` | Get insider purchases only (filtered for buys) |
| `get_insider_roster_holders` | `ticker` | Get insider roster (list of company insiders) |

### Dividends and corporate actions

| Tool | Parameters | Description |
|---|---|---|
| `get_dividends` | `ticker, period="5y"` | Get dividend payment history and current metrics |
| `get_stock_splits` | `ticker` | Get stock split history |
| `get_corporate_actions` | `ticker` | Get all corporate actions (dividends + splits combined) |
| `get_capital_gains` | `ticker` | Get capital gains distributions (primarily for funds/ETFs) |

### Options

| Tool | Parameters | Description |
|---|---|---|
| `get_options_chain` | `ticker, expiration=""` | Get options chain data (calls and puts) |
| `get_options_expirations` | `ticker` | Get all available options expiration dates |

### Market-wide

| Tool | Parameters | Description |
|---|---|---|
| `get_market_status` |  | Check if US stock markets are currently open |
| `get_market_summary` | `region="US"` | Get a market overview for a region: open/closed status plus main indices, futures, bonds and FX |
| `get_market_indices` |  | Get current prices for major market indices |
| `get_market_movers` | `category="day_gainers", count=10` | Get today's market movers from Yahoo Finance screeners |
| `get_trending_tickers` | `count=10` | Get today's most active (trending) US tickers |
| `get_sector_performance` |  | Get performance of major market sectors |
| `get_sector_overview` | `sector="technology"` | Get a sector overview: size, weight, largest companies, industries and sector ETFs |
| `get_industry_overview` | `industry="semiconductors"` | Get an industry overview: largest, best-performing and fastest-growing companies |

### Calendars

| Tool | Parameters | Description |
|---|---|---|
| `get_upcoming_earnings` | `days=7, limit=25` | Get the market-wide earnings calendar (which companies report in the next N days) |
| `get_ipo_calendar` | `days=14, limit=25` | Get upcoming IPOs (exchange, expected date, price range, shares) |
| `get_economic_calendar` | `days=7, limit=30` | Get upcoming economic events (CPI, jobs, GDP, rate decisions) with expected and prior values |
| `get_splits_calendar` | `days=14, limit=25` | Get upcoming stock splits |

### Funds and ETFs

| Tool | Parameters | Description |
|---|---|---|
| `get_fund_overview` | `ticker` | Get overview data for an ETF or mutual fund |
| `get_fund_holdings` | `ticker, limit=25` | Get top holdings for an ETF or mutual fund |
| `get_fund_sector_weights` | `ticker` | Get sector allocation/weights for an ETF or mutual fund |

### Crypto, forex and commodities

| Tool | Parameters | Description |
|---|---|---|
| `get_crypto_price` | `symbol` | Get cryptocurrency price and market data |
| `get_forex_rate` | `pair` | Get foreign exchange (forex) rate for a currency pair |
| `get_commodity_price` | `commodity` | Get commodity/futures price data |

### Compare

| Tool | Parameters | Description |
|---|---|---|
| `compare_stocks` | `tickers` | Compare key metrics across multiple stocks |
| `get_peer_comparison` | `ticker, peers=null` | Compare a stock with its peers on key metrics |
| `get_historical_comparison` | `tickers, period="1y"` | Compare historical price performance of multiple stocks |
| `get_complete_analysis` | `ticker, peers=""` | Complete analysis of a stock, calling every relevant tool |

### News and filings

| Tool | Parameters | Description |
|---|---|---|
| `get_stock_news` | `ticker, limit=10` | Get recent news articles about a stock |
| `get_sec_filings` | `ticker` | Get recent SEC filings (10-K, 10-Q, 8-K, etc.) |

### Utility

| Tool | Parameters | Description |
|---|---|---|
| `search_ticker` | `query` | Search for ticker symbols by company name or keyword |
| `validate_ticker` | `ticker` | Validate if a ticker symbol exists and is tradeable |
| `get_api_status` |  | Get API status and usage information |
| `run_self_test` | `ticker="SPY"` | Run comprehensive self-test of the yfinance-ai tools (64 checks) |

## License

MIT. Data comes from Yahoo Finance through [yfinance](https://github.com/ranaroussi/yfinance) and may be delayed. Not affiliated with Yahoo. For research and education, not investment advice.
