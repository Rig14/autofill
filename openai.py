import os
from openai import OpenAI

AI_MODEL = "gpt-3.5-turbo"

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate_text(input_string: str) -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_string,
            }
        ],
        model=AI_MODEL,
    )

    return chat_completion.choices[0].message.content
