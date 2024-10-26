from langchain import agents
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate

from src.lc_openapi_poc.tools.get_redis_kubernetes import get_redis_kubernetes_client
from src.lc_openapi_poc.tools.get_weather import get_weather
from src.lc_openapi_poc.tools.get_stock_price import get_stock_price


model = "gemini-1.5-pro-001"
llm = ChatVertexAI(
    model_name=model,
    max_tokens=500,
    temperature=0.5,
)

tools = [get_redis_kubernetes_client, get_stock_price, get_weather]

prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),])

agent = agents.create_tool_calling_agent(
    llm,
    tools,
    prompt
)

agent_executor = agents.AgentExecutor(agent=agent, tools=tools, verbose=True)