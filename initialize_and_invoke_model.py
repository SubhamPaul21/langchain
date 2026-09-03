from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    "anthropic:claude-haiku-4-5",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

response = model.invoke("What's the capital of the moon?")

for chunk in response.content:
    print(chunk, end="", flush=True)
