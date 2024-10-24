import pyautogui
import random

Arr = [
    "YouTube",
    "Facebook",
    "WhatsApp Web",
    "Google Translate",
    "Amazon",
    "Instagram",
    "Gmail",
    "ChatGPT",
    "Netflix",
    "Weather",
    "Twitter",
    "Canva",
    "Wordle",
    "TikTok",
    "Satta King",
    "Google Maps",
    "Hotmail",
    "Roblox",
    "Pinterest",
    "Sarekari Result"
]

def write(x, y):
    pyautogui.click(1289, y)
    pyautogui.typewrite(Arr[random.randint(0, len(Arr) - 1
                                           )])
    pyautogui.press("enter")
    pyautogui.countdown(2)

    pyautogui.click(1341, y)
    pyautogui.typewrite(Arr[random.randint(0, len(Arr) - 1)])
    pyautogui.press("enter")
    pyautogui.countdown(2)

    pyautogui.click(1396, y)
    pyautogui.typewrite(Arr[random.randint(0, len(Arr) - 1)])
    pyautogui.press("enter")
    pyautogui.countdown(2)

    pyautogui.click(1456, y)
    pyautogui.typewrite(Arr[random.randint(0, len(Arr) - 1)])
    pyautogui.press("enter")
    pyautogui.countdown(2)


pyautogui.countdown(4)

i = 1
while i <= 30:
    write(1232, 1049)
    i = i + 1
