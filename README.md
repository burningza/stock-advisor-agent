# SA Mining Stock Advisor Agent

Multi-agent AI system for analyzing JSE-listed South African mining companies.

Built with **CrewAI** + **OpenRouter** (any LLM model). Provides research, financial analysis, and buy/hold/sell recommendations for mining stocks.

## Pipeline

1. **Data Researcher** — Pulls income statements and fundamentals via yfinance
2. **News Researcher** — Searches DuckDuckGo for latest mining news & commodity prices
3. **Data Analyst** — Consolidates data with ZAR currency context
4. **Financial Expert** — Makes Buy/Hold/Sell recommendation

## Quick Start

```bash
cp .env.example .env     # Edit with your OpenRouter key
pip install -r requirements.txt
python main.py           # Default: Anglo American (AGL.JO)
```

Override the stock and model via env:

```bash
STOCK_MODEL=anthropic/claude-sonnet-4 python main.py
# Or edit inputs={"stock": "HAR.JO"} in main.py for Harmony Gold
```

## Requirements

- Python 3.10+
- OpenRouter API key
- Dependencies: crewai, yfinance, langchain-community, curl_cffi, python-dotenv
