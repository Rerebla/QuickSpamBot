import pyautogui
import time
import os


script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = "Beemovie.txt"
abs_file_path = os.path.join(script_dir, rel_path)
text = open(abs_file_path, 'r')
time.sleep(5)

for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
