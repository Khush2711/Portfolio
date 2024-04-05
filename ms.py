import pyautogui
import time

interval = 1

try:
    while True:
        x, y = pyautogui.position()
        
    
        pyautogui.moveTo(x + 20, y + 10000, duration=0.2)
        pyautogui.moveTo(x - 10, y - 10, duration=0.2)
        
        time.sleep(interval)
        
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
