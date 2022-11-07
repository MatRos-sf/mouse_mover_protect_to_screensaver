import random
from itertools import cycle
from time import sleep
import pyautogui
from pynput import keyboard
from playsound import playsound

STOP = 0
ALARM = 10
def draw_square():
    screenWidth, screenHeight = pyautogui.size()
    # side
    a = 200
    # locating center of the screen
    middle_x, middle_y = screenWidth // 2, screenHeight // 2

    move = cycle([(middle_x - 200, middle_y - 200), (middle_x + 200, middle_y - 200),
                  (middle_x + 200, middle_y + 200), (middle_x - 200, middle_y + 200)])
    return move


def draw_rectangle():
    screenWidth, screenHeight = pyautogui.size()
    # side
    a = 200
    # locating center of the screen
    middle_x, middle_y = screenWidth // 2, screenHeight // 2

    move = cycle([(middle_x - a * 2, middle_y - 200), (middle_x + a * 2, middle_y - 200),
                  (middle_x + a * 2, middle_y + 200), (middle_x - a * 2, middle_y + 200)])

    return move


def draw_random_position():
    screenWidth, screenHeight = pyautogui.size()

    while True:
        # random position
        x, y = random.randint(1, screenWidth - 1), random.randint(1, screenHeight - 1)
        yield (x, y)

def on_press(key):
    if key == keyboard.Key.esc:
        def stop_loop():
            global STOP
            STOP = 1

        stop = stop_loop()
    return stop

def play(repeat, nameFile='sound.wav'):
    for i in range(repeat):
        playsound(f'sound\\{nameFile}')

def main():

    shape = random.choice([draw_square(), draw_square(), draw_random_position()])
    # count moves
    moves = 0
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while True:

        current_position = pyautogui.position()
        sleep(600)
        new_position = pyautogui.position()

        if current_position == new_position:
            moves += 1
            x, y = next(shape)
            pyautogui.moveTo(x, y, duration=2)
        if moves >= ALARM:
            play(moves//ALARM)

        if STOP == 1:
            break

    print(f"{moves} moves.")

if __name__ == '__main__':
    main()