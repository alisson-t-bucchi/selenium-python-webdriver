import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.remove
class TestBuyHappyRemove1:

    def test_buy_happy_remove_1(self):
        driver = conftest.driver
        home_page = HomePage()
        select_sticker = SelectSticker()
        go_to_cart_page = ShoppingCartPage()
        click_on_happy = ShoppingCartPage()
        remove_happy = ShoppingCartPage()
        empty_cart_page = ShoppingCartPage()


        #open page and find Stickerfy title
        #assert driver.find_element(By.XPATH, "//a[@class='navbar-brand' and text()='Stickerfy']").is_displayed()
        home_page.successful_login()

        #select stickfy Happy
        # driver.find_element(By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cf9']").click()
        select_sticker.sticker_happy()

        #buy stickfy clicking on "Go to cart" button
        #driver.find_element(By.XPATH, "//a[@href='/shopping-cart/' and text()='Go to cart']").click()
        go_to_cart_page.click_go_to_cart_button()

        #remove stickfy clicking on button "Remove 1"
        #driver.find_element(By.XPATH, "//li[contains(., 'Happy')]//button").click()
        click_on_happy.click_on_sticker()

        #driver.find_element(By.XPATH, "//a[@href='/reduce/5dd8e2b26c26d0000a675cf9' and text()='Remove 1']").click()
        remove_happy.remove_sticker()
        #wait = WebDriverWait(driver, 5)
        #wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Add items to the cart']")))
        empty_cart_page.empty_page()



#Formas de encontrar o botão dentro do box que contem a palavra Happy:
#//li[strong/text()='Happy']//button
#"//li[contains(., 'Happy')]//button")