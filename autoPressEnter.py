import pyautogui
import time
import keyboard  # To detect key presses

# Interval in seconds
interval = 60
count = 0

print("Press 's' to start the Auto Enter program. Press Ctrl+C to stop.")

# Wait for the user to press 's' to start the program
keyboard.wait('s')
print("Auto Enter program started.")

try:
    while True:
        pyautogui.press('enter')
        count += 1
        print("Pressed Enter " + str(count))
        time.sleep(interval)
except KeyboardInterrupt:
    print("Program stopped.")
