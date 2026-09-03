import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()


def test_claude():
    claude_api_key = os.getenv("CLAUDE_API_KEY")
    model = ChatAnthropic(
        api_key=claude_api_key,
        model_name="claude-haiku-4-5",
        timeout=30,
        stop=None,
    )

    messages = [
        (
            "system",
            "You are a helpful translator. Translate the user sentence to French.",
        ),
        (
            "human",
            "I love programming.",
        ),
    ]

    for chunk in model.stream(messages):
        print(chunk.content, end="", flush=True)


if __name__ == "__main__":
    test_claude()
