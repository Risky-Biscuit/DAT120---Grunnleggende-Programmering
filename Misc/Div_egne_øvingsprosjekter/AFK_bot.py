import pyautogui as pag
import random
import time

# Infinite loop to keep the bot running
while True:
    # Generate random x and y coordinates within specified ranges
    x = random.randint(600, 700)
    y = random.randint(100, 200)

    # Move the mouse to the generated coordinates over 0.5 seconds
    pag.moveTo(x, y, duration=0.5)

    # Pause for 2 seconds before the next iteration
    time.sleep(2)