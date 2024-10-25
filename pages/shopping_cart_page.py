import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    def __init__(self): #construtor da classe
        self.driver = conftest.driver
        self.go_to_cart_button = (By.XPATH, "//a[@href='/shopping-cart/' and text()='Go to cart']")

    def click_go_to_cart_button(self):
        self.click(self.go_to_cart_button)