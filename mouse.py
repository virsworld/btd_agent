import pyautogui
from pyautogui import ImageNotFoundException
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def place_monkey(type: str, location: tuple[int, int]) -> None:
    time.sleep(3) # for testing
    try:
        x, y = pyautogui.locateCenterOnScreen(f"{SCRIPT_DIR}/monkeys/{type}.png", grayscale=False, confidence=0.3)
        print(f"Found monkey {type} at: ", (int(x), int(y)))
        pyautogui.click(x, y)
        pyautogui.click(location[0], location[1])
        print(f"Placed monkey {type} at: ", location)
    except ImageNotFoundException as e:
        print("Error finding monkey: ", e)
    except Exception as e:
        print("Error placing monkey: ", str(e))

def test():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr, end="\r")
    except KeyboardInterrupt:
        print("\n")

if __name__ == "__main__":
    place_monkey("dart_mky", (1920 / 2, 1080 / 2))

#TODO: make functions to place monkeys