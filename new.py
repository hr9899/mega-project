import pyautogui
import pyperclip
import time
import google.generativeai as genai

# ---------- SETTINGS ----------
GEMINI_API_KEY = "AIzaSyBxum9WekmzxZ3PQ7RLkVKDRupb3Ae5vQI"  # put your API key
pyautogui.FAILSAFE = False  # optional: disable safety
# ------------------------------

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Wait a few seconds to prepare
time.sleep(3)

# Step 1: Click the icon
pyautogui.click(1639, 1412)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(1003, 237, duration=0.5)
pyautogui.dragTo(2187, 1258, duration=1.0, button='left')
time.sleep(0.5)

# Step 3: Copy the selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get the copied text
copied_text = pyperclip.paste()
print("Copied text:\n", copied_text)

# Step 5: Send to Gemini for processing
prompt = f"Summarize or understand this text:\n\n{copied_text}"
response = model.generate_content(prompt)

# Step 6: Print Gemini response
print("\nGemini Response:\n")
print(response.text)
