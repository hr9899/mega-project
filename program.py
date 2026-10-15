import pyautogui
import time
import pyperclip
pyautogui.FAILSAFE = False

# Small delay to let you switch to the right window
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(1639, 1412)
time.sleep(1)  # wait for any window to open

# Step 2: Drag to select text
pyautogui.moveTo(507, 222, duration=0.5)
pyautogui.dragTo(626, 687, duration=1.0, button='left')
time.sleep(0.5)

# Step 3: Copy selected text (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click()
time.sleep(0.5)

# Step 4: Get copied text from clipboard
copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)
