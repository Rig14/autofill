import keyboard

from api import generate_text

GENERATE_TEXT_SHORTCUT = "ctrl+alt+space"
CLEAR_CACHE_SHORTCUT = "ctrl+alt+c"
TEXT_WRITING_SPEED = 0.03

inputs: list[keyboard.KeyboardEvent] = []


def get_text() -> str:
    """Get the text that user has typed, since the last time the shortcut was pressed.

    Returns:
        str: The text that user has typed.
    """
    keyboard.wait(GENERATE_TEXT_SHORTCUT)
    generator = keyboard.get_typed_strings(inputs)
    text = "".join([text for text in generator if text])
    print(text)
    return text


def type_text(text: str) -> None:
    """Type the given text.

    Args:
        text (str): The text to type.
    """
    try:
        for line in text.split("\n"):
            keyboard.write(line, delay=TEXT_WRITING_SPEED)
            keyboard.press_and_release("enter")
    except StopIteration:
        print(text)
        print("Text generation stopped.")


def main():
    keyboard.hook(inputs.append)
    keyboard.add_hotkey(CLEAR_CACHE_SHORTCUT, lambda: inputs.clear())
    while True:
        res = get_text()
        generated_text = generate_text(res)
        type_text(generated_text)


if __name__ == "__main__":
    main()
