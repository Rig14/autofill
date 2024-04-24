import keyboard
import string

from api import generate_text

GENERATE_TEXT_SHORTCUT = "ctrl+alt+space"
TEXT_WRITING_SPEED = 0.03


def get_text():
    inputs = keyboard.record(GENERATE_TEXT_SHORTCUT)
    generator = keyboard.get_typed_strings(inputs)
    text = "".join([text for text in generator if text])

    return text


def type_text(text: str) -> None:
    # clean text
    text = "".join([x for x in text if x in string.ascii_letters + " "])
    keyboard.write(text, delay=TEXT_WRITING_SPEED)


def main():
    # listen for keyboard input and store it in a list
    while True:
        res = get_text()
        generated_text = generate_text(res)
        type_text(generated_text)


if __name__ == "__main__":
    main()
