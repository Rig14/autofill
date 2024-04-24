import os
from openai import OpenAI
from dotenv import load_dotenv

AI_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 100

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def generate_text(input_string: str) -> str:
    """Generates text using the OpenAI API when ``input_string`` is provided.

    Args:
        input_string (str): The input string to generate text from.

    Returns:
        str: The generated text.
    """
    if not input_string:
        return ""

    response = client.chat.completions.create(
        model=AI_MODEL,
        messages=[{"role": "user", "content": input_string}],
        temperature=1,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    input_string = "This will need to be"
    print(generate_text(input_string))
