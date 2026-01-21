import pyautogui

print("Press Ctrl-C to quit.")


def test():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr, end="\r")
    except KeyboardInterrupt:
        print("\n")


if __name__ == "__main__":
    test()
