import keyboard
import string

from api import generate_text

GENERATE_TEXT_SHORTCUT = "ctrl+alt+space"


def get_text():
    keys: list[keyboard.KeyboardEvent] = []
    keyboard.hook(keys.append)
    keyboard.wait(GENERATE_TEXT_SHORTCUT)
    keyboard.unhook_all()

    res = ""
    for key in keys:
        if key.event_type == keyboard.KEY_DOWN:
            name = key.name
            if name == "space":
                res += " "
                continue

            if name not in string.ascii_letters:
                continue
            else:
                res += name

    return res


def main():
    # listen for keyboard input and store it in a list
    res = get_text()
    generated_text = generate_text(res)
    print(generated_text)


if __name__ == "__main__":
    main()
