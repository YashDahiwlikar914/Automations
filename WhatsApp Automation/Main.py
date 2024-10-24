import time

from selenium import webdriver

from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage

driver = webdriver.Chrome()
driver.maximize_window()

pane_page = PanePage(driver)

opened_chats = pane_page.opened_chats

for oc in opened_chats:
    print(oc.name)  # contact name (as appears on your whatsapp)
    print(oc.icon)  # the url of the image
    print(oc.last_message)
    print(oc.last_message_time)  # datetime object
    print(oc.has_notifications())  # are there unread messages?
    print(oc.notifications)  # returns a integer with the qty of new messages, if there are.

first_chat = opened_chats[0]
first_chat.click()

chat_page = ChatPage(driver)
msgs = chat_page.messages.newest(10, filterby='contact')

for msg in msgs:
    print(msg.contact) # name (all should be the same)
    print(msg.date)
    print(msg.text)
    print(msg.status)

driver.quit()