import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SelectSticker(BasePage):
    def __init__(self): #construtor da classe
        self.driver = conftest.driver
        self.href_happy = (By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cf9']")
        self.href_sad = (By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cfb']")
        self.href_angry = (By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cfa']")


    def sticker_happy(self):
        self.click(self.href_happy)

    def sticker_sad(self):
        self.click(self.href_sad)

    def sticker_angry(self):
        self.click(self.href_angry)

    def all_stickers(self):
        self.click(self.href_happy)
        self.click(self.href_angry)
        self.click(self.href_sad)

    def select_2_happy(self):
        self.double_click(self.href_happy)


