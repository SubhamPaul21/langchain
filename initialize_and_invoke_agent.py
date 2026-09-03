from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

agent = create_agent(
    model="anthropic:claude-haiku-4-5",
    tools=None,
    system_prompt="You are a helpful assistant. Be concise and accurate.",
)

response = agent.invoke(
    {
        "messages": [
            HumanMessage(content="What's the capital of the moon?"),
        ],
    }
)

print(response)
