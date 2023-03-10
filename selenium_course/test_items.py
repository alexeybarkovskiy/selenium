import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    assert button, "Button is not found"
