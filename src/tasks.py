from crewai import Task

from src.agents import analyst, data_explorer, fin_expert, news_info_explorer

# Task to gather financial data of a mining stock
get_company_financials = Task(
    description="Get financial data like income statements and other fundamental ratios for mining stock: {stock}",
    expected_output="Detailed information from income statement, key ratios for {stock}. "
    "Indicate also about current financial status and trend over the period. Use ZAR (South African Rands) for currency.",
    agent=data_explorer,
)

# Task to gather company news
get_company_news = Task(
    description="Get latest news and business information about mining company: {stock}. "
    "Include commodity price movements, and South African mining regulatory updates",
    expected_output="Latest news and business information about the mining company. Provide a summary also.",
    agent=news_info_explorer,
)

# Task to analyze financial data and news
analyse = Task(
    description="Make thorough analysis based on given financial data and latest news of a mining stock",
    expected_output="Comprehensive analysis of a mining stock outlining financial health, stock valuation, risks, and news. "
    "Mention currency in ZAR (South African Rands) and consider commodity price context.",
    agent=analyst,
    context=[get_company_financials, get_company_news],
)

# Task to provide financial advice
advise = Task(
    description="Make a recommendation about investing in a mining stock, based on analysis provided and current stock price. "
    "Explain the reasons.",
    expected_output="Recommendation (Buy / Hold / Sell) of a mining stock backed with reasons elaborated. "
    "Response in Markdown format.",
    agent=fin_expert,
    context=[analyse],
)