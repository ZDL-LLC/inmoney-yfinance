# yfinance-ai MCP server

<!-- mcp-name: io.github.lkcair/yfinance-ai -->

[![PyPI](https://img.shields.io/pypi/v/yfinance-ai)](https://pypi.org/project/yfinance-ai/) [![Python](https://img.shields.io/pypi/pyversions/yfinance-ai)](https://pypi.org/project/yfinance-ai/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![MCP Registry](https://img.shields.io/badge/MCP%20Registry-io.github.lkcair%2Fyfinance--ai-blue)](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.lkcair/yfinance-ai)

**Yahoo Finance for Claude, Cursor, VS Code and any MCP client, in 68 tools.** Real-time quotes, history, financial statements, ratios and valuation history, analyst estimates and price targets, earnings, dividends, options, holders and insiders, funds and ETFs, crypto, forex, commodities, market movers, sectors and industries, and earnings, IPO, economic and split calendars.

Powered by [**yfinance-ai**](https://github.com/lkcair/yfinance-ai), the Yahoo Finance toolkit with **thousands of downloads on ClawHub and OpenWebUI**.

| Also available as | |
|---|---|
| 🦞 OpenClaw skill, thousands of downloads | `openclaw skills install @lkcair/stocks` ([ClawHub](https://clawhub.ai/lkcair/stocks), [skill repo](https://github.com/lkcair/yfinance-ai-skill)) |
| 🌐 OpenWebUI tool, thousands of downloads | [openwebui.com](https://openwebui.com/posts/finance_data_pull_ai_tool_yahoo_finance_yfinance_fc928bb1) ([source](https://github.com/lkcair/yfinance-ai)) |
| 📑 SEC EDGAR filings, same family | [sec-ai MCP server](https://github.com/lkcair/sec-ai-mcp) |

## Install: one command

Needs [uv](https://docs.astral.sh/uv/getting-started/installation/). No API key, no account, no Docker.

**Claude Code**
```bash
claude mcp add yfinance-ai -- uvx yfinance-ai@latest
```

**VS Code**
```bash
code --add-mcp '{"name":"yfinance-ai","type":"stdio","command":"uvx","args":["yfinance-ai@latest"]}'
```

**Claude Desktop, Cursor, Windsurf and any other MCP client**: add to the client's MCP config (`claude_desktop_config.json`, `.cursor/mcp.json`, ...)
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

`@latest` checks PyPI on each start, so you always run the newest release. Without uv: `pip install yfinance-ai` and use `"command": "yfinance-ai"` with no args.

## Ask it anything

- "Compare AAPL, MSFT and GOOGL on valuation and margins"
- "What are analysts saying about NVIDIA? Price targets and recent upgrades"
- "Is Apple buying back shares? Show shares outstanding over 5 years"
- "Who reports earnings this week?" / "Economic calendar for this week" / "Upcoming IPOs"
- "Top gainers today" / "Semiconductor industry: largest and fastest-growing companies"
- "SPY top holdings and sector weights" / "Options chain for TSLA, nearest expiry"
- "Bitcoin price" / "EUR/USD rate" / "Gold and oil today"

## Why yfinance-ai

- **68 tools**, more than four times the most-starred yfinance MCP servers (15 and 9 tools), covering everything above in one server.
- **Answers written for an AI**: readable text with context, not raw dataframes.
- **Numbers checked at every release** against independent sources: revenue, net income, assets and TTM figures against SEC XBRL filings, prices and ratios against a second Yahoo endpoint.
- **Every tool is read-only** (MCP annotations), with retries, validation and rate limiting.
- **The same toolkit runs everywhere**: MCP, OpenClaw and OpenWebUI, with thousands of downloads on ClawHub and OpenWebUI.
- **Built-in self-test**: ask "run the yfinance self-test".

## Tools (68)

### Quotes and history

| Tool | Parameters | What it does |
|---|---|---|
| `get_stock_price` | `ticker` | Get current stock price and key metrics for a ticker symbol |
| `get_stock_quote` | `ticker` | Get detailed quote with bid/ask, day range, and trading info |
| `get_fast_info` | `ticker` | Get fast-access ticker information (lightweight, quick response) |
| `get_historical_data` | `ticker, period="1y", interval="1d"` | Get historical price data for a stock |
| `get_historical_price_on_date` | `ticker, date` | Get historical price for a specific date |
| `download_multiple_tickers` | `tickers, period="1mo", interval="1d"` | Download historical data for multiple tickers at once (bulk operation) |

### Company

| Tool | Parameters | What it does |
|---|---|---|
| `get_company_info` | `ticker` | Get detailed company information and business description |
| `get_company_overview` | `ticker` | Company overview with context for every metric |
| `get_company_officers` | `ticker` | Get company officers and key management |
| `get_isin` | `ticker` | Get International Securities Identification Number (ISIN) for a ticker |

### Financials

| Tool | Parameters | What it does |
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

| Tool | Parameters | What it does |
|---|---|---|
| `get_earnings_dates` | `ticker` | Get upcoming and past earnings dates with estimates |
| `get_earnings_history` | `ticker` | Get historical earnings data with annual and quarterly figures |
| `get_earnings_calendar` | `ticker` | Get earnings calendar including next earnings date and dividend dates |
| `get_analyst_estimates` | `ticker` | Get analyst estimates for earnings, revenue, and EPS |
| `get_growth_estimates` | `ticker` | Get analyst growth estimates |
| `get_eps_trend` | `ticker` | Get EPS (Earnings Per Share) trend data showing how estimates have changed |
| `get_eps_revisions` | `ticker` | Get EPS revision data showing analyst estimate changes |

### Analysts

| Tool | Parameters | What it does |
|---|---|---|
| `get_analyst_recommendations` | `ticker` | Get analyst recommendations and ratings |
| `get_analyst_price_targets` | `ticker` | Get detailed analyst price targets for a stock |
| `get_upgrades_downgrades` | `ticker, limit=20` | Get detailed analyst upgrades and downgrades history |

### Holders and insiders

| Tool | Parameters | What it does |
|---|---|---|
| `get_institutional_holders` | `ticker` | Get major institutional holders and their ownership |
| `get_major_holders` | `ticker` | Get major holders summary (institutions, insiders, public float) |
| `get_mutualfund_holders` | `ticker` | Get mutual fund holders |
| `get_insider_transactions` | `ticker` | Get recent insider trading activity |
| `get_insider_purchases` | `ticker` | Get insider purchases only (filtered for buys) |
| `get_insider_roster_holders` | `ticker` | Get insider roster (list of company insiders) |

### Dividends and corporate actions

| Tool | Parameters | What it does |
|---|---|---|
| `get_dividends` | `ticker, period="5y"` | Get dividend payment history and current metrics |
| `get_stock_splits` | `ticker` | Get stock split history |
| `get_corporate_actions` | `ticker` | Get all corporate actions (dividends + splits combined) |
| `get_capital_gains` | `ticker` | Get capital gains distributions (primarily for funds/ETFs) |

### Options

| Tool | Parameters | What it does |
|---|---|---|
| `get_options_chain` | `ticker, expiration=""` | Get options chain data (calls and puts) |
| `get_options_expirations` | `ticker` | Get all available options expiration dates |

### Market-wide

| Tool | Parameters | What it does |
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

| Tool | Parameters | What it does |
|---|---|---|
| `get_upcoming_earnings` | `days=7, limit=25` | Get the market-wide earnings calendar (which companies report in the next N days) |
| `get_ipo_calendar` | `days=14, limit=25` | Get upcoming IPOs (exchange, expected date, price range, shares) |
| `get_economic_calendar` | `days=7, limit=30` | Get upcoming economic events (CPI, jobs, GDP, rate decisions) with expected and prior values |
| `get_splits_calendar` | `days=14, limit=25` | Get upcoming stock splits |

### Funds and ETFs

| Tool | Parameters | What it does |
|---|---|---|
| `get_fund_overview` | `ticker` | Get overview data for an ETF or mutual fund |
| `get_fund_holdings` | `ticker, limit=25` | Get top holdings for an ETF or mutual fund |
| `get_fund_sector_weights` | `ticker` | Get sector allocation/weights for an ETF or mutual fund |

### Crypto, forex and commodities

| Tool | Parameters | What it does |
|---|---|---|
| `get_crypto_price` | `symbol` | Get cryptocurrency price and market data |
| `get_forex_rate` | `pair` | Get foreign exchange (forex) rate for a currency pair |
| `get_commodity_price` | `commodity` | Get commodity/futures price data |

### Compare

| Tool | Parameters | What it does |
|---|---|---|
| `compare_stocks` | `tickers` | Compare key metrics across multiple stocks |
| `get_peer_comparison` | `ticker, peers=null` | Compare a stock with its peers on key metrics |
| `get_historical_comparison` | `tickers, period="1y"` | Compare historical price performance of multiple stocks |
| `get_complete_analysis` | `ticker, peers=""` | Complete analysis of a stock, calling every relevant tool |

### News and filings

| Tool | Parameters | What it does |
|---|---|---|
| `get_stock_news` | `ticker, limit=10` | Get recent news articles about a stock |
| `get_sec_filings` | `ticker` | Get recent SEC filings (10-K, 10-Q, 8-K, etc.) |

### Utility

| Tool | Parameters | What it does |
|---|---|---|
| `search_ticker` | `query` | Search for ticker symbols by company name or keyword |
| `validate_ticker` | `ticker` | Validate if a ticker symbol exists and is tradeable |
| `get_api_status` |  | Get API status and usage information |
| `run_self_test` | `ticker="SPY"` | Run comprehensive self-test of the yfinance-ai tools (64 checks) |

## License

MIT. Data comes from Yahoo Finance through [yfinance](https://github.com/ranaroussi/yfinance) and may be delayed. Not affiliated with Yahoo. For research and education, not investment advice.
