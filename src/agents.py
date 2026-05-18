import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

from src.tools import (
    get_company_info,
    get_current_stock_price,
    get_income_statements,
    search_tool,
)
from src.utils import Today

load_dotenv()

llm = LLM(
    model=os.getenv("STOCK_MODEL", "openai/gpt-4o"),
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)

# Agent for gathering company news and information
news_info_explorer = Agent(
    role="News and Info Researcher",
    goal="Gather and provide the latest news and information about a mining company from the internet",
    llm=llm,
    verbose=True,
    backstory=(
        "You are an expert researcher, who can gather detailed information about a mining company. "
        "Focus on South African mining sector news, commodity prices, and regulatory changes. "
        "Consider you are on: " + Today
    ),
    tools=[search_tool],
    cache=True,
    max_iter=5,
)

# Agent for gathering financial data
data_explorer = Agent(
    role="Data Researcher",
    goal="Gather and provide financial data and company information about a mining stock on the JSE",
    llm=llm,
    verbose=True,
    backstory=(
        "You are an expert researcher, who can gather detailed information about a mining company or stock. "
        'When using tools, use the stock symbol and add a suffix ".JO" to it for JSE listings. '
        "Try with and without the suffix and see what works. "
        "Consider you are on: " + Today
    ),
    tools=[get_company_info, get_income_statements],
    cache=True,
    max_iter=5,
)

# Agent for analyzing data
analyst = Agent(
    role="Data Analyst",
    goal="Consolidate financial data, stock information, and provide a summary for a mining company",
    llm=llm,
    verbose=True,
    backstory=(
        "You are an expert in analyzing financial data, mining/commodity-related current information, and "
        "making a comprehensive analysis. Use South African Rands (ZAR) for currency. "
        "Consider you are on: " + Today
    ),
)

# Agent for financial recommendations
fin_expert = Agent(
    role="Financial Expert",
    goal="Considering financial analysis of a mining stock, make investment recommendations",
    llm=llm,
    verbose=True,
    tools=[get_current_stock_price],
    max_iter=5,
    backstory=(
        "You are an expert financial advisor specializing in the South African mining sector. "
        "You can provide investment recommendations. "
        "Consider the financial analysis, current information about the company, current stock price, "
        "commodity prices, and make recommendations about whether to buy/hold/sell a stock along with reasons. "
        'When using tools, try with and without the suffix ".JO" to the stock symbol for JSE listings. '
        "Consider you are on: " + Today
    ),
)