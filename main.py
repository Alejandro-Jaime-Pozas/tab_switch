import pyautogui
import time

def switch_app():
    print("Switching application with Alt+Tab")
    pyautogui.keyDown('alt')        # Hold down Alt
    pyautogui.press('tab')          # Press Tab
    time.sleep(0.1)                 # Short delay to ensure it registers
    pyautogui.keyUp('alt')          # Release Alt

if __name__ == "__main__":
    print("Starting app switcher. Press Ctrl+C to stop.")
    try:
        while True:
            switch_app()
            time.sleep(15)  # Wait 15 seconds
    except KeyboardInterrupt:
        print("Stopped by user.")
