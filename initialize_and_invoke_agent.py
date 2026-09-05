from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from pprint import pprint
from pydantic import BaseModel

load_dotenv()


class CapitalInfo(BaseModel):
    name: str
    location: str
    time_zone: str
    economic_activity: str


agent = create_agent(
    model="anthropic:claude-haiku-4-5",
    tools=None,
    system_prompt="You are a science fiction writer. Be concise and accurate.",
    response_format=CapitalInfo,
)

# Getting answers after it's processed
response = agent.invoke(
    {
        "messages": [
            HumanMessage(content="What's the capital of the moon?"),
        ],
    }
)

pprint(response)

# Getting answers as they are processed by streaming the output
# for token, metadata in agent.stream(
#     {
#         "messages": [
#             HumanMessage(content="What's the capital of the moon?"),
#         ],
#     },
#     stream_mode="messages",
# ):
#     if token.content:  # type: ignore
#         print(token.content, end="", flush=True)  # type: ignore
