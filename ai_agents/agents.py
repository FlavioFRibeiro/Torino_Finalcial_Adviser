# ai_agents/agents.py

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

agente_web_search = Agent(
    name="Torino Agente Web Search",
    role="Fazer busca na web",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[DuckDuckGo()],
    instructions=["Sempre inclua as fontes"],
    show_tool_calls=True,
    markdown=True
)

agente_financeiro = Agent(
    name="Torino Agente Financeiro",
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True
    )],
    instructions=["Sempre use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent = Agent(
    team=[agente_web_search, agente_financeiro],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Sempre inclua as fontes",
                  "Sempre use tabelas para mostrar os dados"],
    show_tool_calls=True,
    markdown=True
)