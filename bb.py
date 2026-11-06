import time
import random
from rich.live import Live

WIDTH = 60
HEIGHT = 20


def draw():
    screen = ""

    for y in range(HEIGHT):
        for x in range(WIDTH):

            if random.random() < 0.05:
                screen += "#"
            else:
                screen += "."

        screen += "\n"

    return screen


with Live(refresh_per_second=15, screen=True) as live:

    for i in range(100):
        live.update(draw())
        time.sleep(0.1)