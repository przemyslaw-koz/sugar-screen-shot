import pyautogui
import datetime

# Get screenshot
screenshot = pyautogui.screenshot()

# Create file name with timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"screenshot_{timestamp}.png"

# Save screenshot
screenshot.save(file_name)

print(f"Zrzut ekranu zapisany jako {file_name}")
