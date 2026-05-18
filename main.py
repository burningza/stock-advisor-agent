from datetime import datetime

from crewai import Crew, Process

from src.agents import analyst, data_explorer, fin_expert, news_info_explorer
from src.tasks import advise, analyse, get_company_financials, get_company_news
from src.utils import timestamp

# Stock symbol — change this to whatever you want to analyze
STOCK = "AGL.JO"

# Date-time stamp for unique filenames
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
stock_clean = STOCK.replace(".", "-")

# Set dynamic output filenames
analyse.output_file = f"Analysis_{stock_clean}_{ts}.md"
advise.output_file = f"Recommendation_{stock_clean}_{ts}.md"

# Define the crew with agents and tasks in sequential process
crew = Crew(
    agents=[data_explorer, news_info_explorer, analyst, fin_expert],
    tasks=[get_company_financials, get_company_news, analyse, advise],
    verbose=True,
    Process=Process.sequential,
    step_callback=timestamp,
)

# Run the crew with a specific mining stock (JSE-listed)
result = crew.kickoff(inputs={"stock": STOCK})

# Print the final result
print("Final Result:", result)