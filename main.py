import keyboard
import string


def get_text():
    keys: list[keyboard.KeyboardEvent] = []
    keyboard.hook(keys.append)
    keyboard.wait("esc")
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
    print(res)


if __name__ == "__main__":
    main()
