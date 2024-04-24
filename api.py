import os
from openai import OpenAI
from dotenv import load_dotenv

AI_MODEL = "babbage-002"
MAX_TOKENS = 50

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate_text(input_string: str) -> str:
    response = client.completions.create(
        model=AI_MODEL,
        prompt=input_string,
        temperature=1,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].text


if __name__ == "__main__":
    input_string = "Hello, how are you doing"
    print(generate_text(input_string))
