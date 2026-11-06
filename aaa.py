import os
import sys
import time

def spiral_wipe(speed=0.005):
    # Hide cursor and clear screen first
    sys.stdout.write("\033[?25l\033[2J\033[H")
    sys.stdout.flush()

    try:
        columns, rows = os.get_terminal_size()
    except OSError:
        columns, rows = 80, 24

    top, bottom = 0, rows - 1
    left, right = 0, columns - 1

    # Light blue/cyan block character
    block_char = "\033[36m█"

    while top <= bottom and left <= right:
        # Move right along the top boundary
        for x in range(left, right + 1):
            sys.stdout.write(f"\033[{top+1};{x+1}H{block_char}")
            sys.stdout.flush()
            time.sleep(speed)
        top += 1

        # Move down along the right boundary
        for y in range(top, bottom + 1):
            sys.stdout.write(f"\033[{y+1};{right+1}H{block_char}")
            sys.stdout.flush()
            time.sleep(speed)
        right -= 1

        # Move left along the bottom boundary
        if top <= bottom:
            for x in range(right, left - 1, -1):
                sys.stdout.write(f"\033[{bottom+1};{x+1}H{block_char}")
                sys.stdout.flush()
                time.sleep(speed)
            bottom -= 1

        # Move up along the left boundary
        if left <= right:
            for y in range(bottom, top - 1, -1):
                sys.stdout.write(f"\033[{y+1};{left+1}H{block_char}")
                sys.stdout.flush()
                time.sleep(speed)
            left += 1

    # Hold the final screen for a brief moment, then clear and restore cursor
    time.sleep(0.5)
    sys.stdout.write("\033[?25h\033[2J\033[H\033[0m")
    sys.stdout.flush()

if __name__ == "__main__":
    spiral_wipe()
