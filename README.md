# Selenium Project - Page Object Model (POM)

This project uses the Page Object Model (POM) pattern for automated tests with Selenium. It was developed to test the [Stickerfy](https://stickerfy.herokuapp.com/) website and organizes test scenarios for different interactions on the site.

## Project Structure

```
selenium-project-pom/
|-- .venv/                              # Virtual environment containing dependencies
|-- conftest.py                         # Global configurations and pytest fixtures
|-- pages/                              # POM files representing the site pages
|   |-- __init__.py                     # Makes the folder a Python module
|   |-- base_page.py                    # Base class with reusable generic methods
|   |-- checkout_page.py                # Represents the checkout page
|   |-- home_page.py                    # Represents the homepage
|   |-- select_sticker.py               # Manages sticker selection
|   |-- shopping_cart_page.py           # Manages interactions on the shopping cart page
|-- tests/                              # Tests organized by scenario
    |-- using_go_to_cart_button/        # Tests for the "Go to Cart" button
    |-- using_remove_1_button/          # Tests for removing items
    |-- using_shopping_cart_button/     # Tests for the "Shopping Cart" button
```

## Prerequisites

1. Python 3.8 or higher installed.
2. Google Chrome installed.
3. ChromeDriver compatible with your Chrome version.
4. Install project dependencies:

```bash
pip install selenium pytest
```

## Project Pattern (POM)

The Page Object Model pattern organizes code so that interaction logic with the interface is separate from the tests. This facilitates maintenance and reuse.

- **`base_page.py`**:
  Contains reusable generic methods, such as clicking on elements or locating them.

- **Other files in `pages/`**:
  Each file represents a page of the site, encapsulating specific elements and their interactions.

Example of a method in `base_page.py`:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
```

## Running the Tests

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd selenium-project-pom
```

3. Run the tests:

```bash
pytest tests/
```

The results will be displayed in the console.

## Test Structure

Tests are organized by scenario within the `tests/` folder. Each subfolder represents a specific flow:

1. **`using_go_to_cart_button/`**:
   Tests navigation to the cart using the "Go to Cart" button.

2. **`using_remove_1_button/`**:
   Validates the removal of items from the cart.

3. **`using_shopping_cart_button/`**:
   Tests navigation to the cart using the "Shopping Cart" button.

Example of a test:

```python
def test_go_to_cart(driver):
    home_page = HomePage(driver)
    home_page.add_item_to_cart()
    home_page.go_to_cart()

    cart_page = ShoppingCartPage(driver)
    assert cart_page.is_cart_page_displayed()
```

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements.

## License

This project is licensed under the MIT License.