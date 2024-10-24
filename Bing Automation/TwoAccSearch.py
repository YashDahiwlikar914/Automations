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
    "Sarekari Result",
    "Technology",
    "Social Media",
    "Gaming",
    "Entertainment",
    "News and Politics",
    "Health and Wellness",
    "Education",
    "Travel",
    "Finance and Investing",
    "Fashion and Beauty",
    "Anime and Manga",
    "Cosplay",
    "DIY and Crafts",
    "Book Reviews and Recommendations",
    "Food and Cooking",
    "Artificial Intelligence",
    "Virtual Reality and Augmented Reality",
    "Cryptocurrency and Blockchain",
    "Climate Change and Sustainability",
    "E-commerce and Online Shopping"
]


def timer():
    pyautogui.countdown(3)


def write():
    pyautogui.typewrite(Arr[random.randint(0, len(Arr) - 1)])
    pyautogui.press('enter')
    pyautogui.countdown(2)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('alt', 'tab')


pyautogui.countdown(4)

i = 1
while i <= 60:
    write()
    timer()
    i = i + 1
