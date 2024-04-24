import keyboard

from api import generate_text

GENERATE_TEXT_SHORTCUT = "ctrl+alt+space"
TEXT_WRITING_SPEED = 0.03


def get_text() -> str:
    """Get the text that user has typed, since the last time the shortcut was pressed.

    Returns:
        str: The text that user has typed.
    """
    inputs = keyboard.record(GENERATE_TEXT_SHORTCUT)
    generator = keyboard.get_typed_strings(inputs)
    text = "".join([text for text in generator if text])

    return text


def type_text(text: str) -> None:
    """Type the given text.

    Args:
        text (str): The text to type.
    """
    keyboard.write(text, delay=TEXT_WRITING_SPEED)


def main():
    while True:
        res = get_text()
        generated_text = generate_text(res)
        type_text(generated_text)


if __name__ == "__main__":
    main()
