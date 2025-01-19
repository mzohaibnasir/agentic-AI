from phi.agent import Agent
from phi.model.groq import Groq  # model
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo  # for web surfing
import openai


import os
import phi
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


phi.api = os.getenv("PHI_API_KEY")


# web search agent
websearch_agent = Agent(
    name="Web search agent",
    role="Search the web for the information",
    model=Groq(id="llama3-8b-8192"),
    tools=[
        DuckDuckGo(),
    ],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


# financial agent
finance_agent = Agent(
    name="Finance AI agent",
    model=Groq(id="llama3-8b-8192"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)


app = Playground(agents=[finance_agent, websearch_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
