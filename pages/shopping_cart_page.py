import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    def __init__(self): #construtor da classe
        self.driver = conftest.driver
        self.go_to_cart_button = (By.XPATH, "//a[@href='/shopping-cart/' and text()='Go to cart']")
        self.have_happy = (By.XPATH, "//li[contains(., 'Happy')]//button")
        self.have_sad = (By.XPATH, "//li[contains(., 'Sad')]//button")
        self.have_angry = (By.XPATH, "//li[contains(., 'Angry')]//button")
        self.remove_happy = (By.XPATH, "//a[@href='/reduce/5dd8e2b26c26d0000a675cf9' and text()='Remove 1']")
        self.empty_shopping_cart = (By.XPATH, "//h2[text()='Add items to the cart']")

    def click_go_to_cart_button(self):
        self.click(self.go_to_cart_button)

    def verify_all_stickers(self):
        self.find_elements(self.have_happy)
        self.find_elements(self.have_sad)
        self.find_elements(self.have_angry)

    def click_on_sticker(self):
        self.click(self.have_happy)

    def remove_sticker(self):
        self.click(self.remove_happy)

    def empty_page(self):
        self.wait_element(self.empty_shopping_cart)
