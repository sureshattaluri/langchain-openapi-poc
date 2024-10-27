from langchain import agents
from langchain_mongodb import MongoDBChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.lc_openapi_poc.mongodb.mongodb_chat_history import connection_string, database_name, collection_name
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
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

agent = agents.create_tool_calling_agent(
    llm,
    tools,
    prompt
)

agent_executor = agents.AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_with_history = RunnableWithMessageHistory(
        agent_executor,
        lambda session_id: MongoDBChatMessageHistory(
            session_id=session_id,
            connection_string=connection_string,
            database_name=database_name,
            collection_name=collection_name,
        ),
        input_messages_key="input",
        history_messages_key="chat_history",
    )
