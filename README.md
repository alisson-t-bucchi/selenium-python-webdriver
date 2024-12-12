# Selenium Project - Page Object Model (POM)

Este projeto utiliza o padrão Page Object Model (POM) para testes automatizados com Selenium. Ele foi desenvolvido para testar o website [Stickerfy](https://stickerfy.herokuapp.com/) e organiza cenários de teste para diferentes interações no site.

## Estrutura do Projeto

```
selenium-project-pom/
|-- .venv/                   # Ambiente virtual contendo dependências
|-- conftest.py              # Configurações globais e fixtures do pytest
|-- pages/                   # Arquivos POM representando as páginas do site
|   |-- __init__.py          # Torna a pasta um módulo Python
|   |-- base_page.py         # Classe base com métodos genéricos reutilizáveis
|   |-- checkout_page.py     # Representa a página de checkout
|   |-- home_page.py         # Representa a página inicial
|   |-- select_sticker.py    # Gerencia a seleção de adesivos
|   |-- shopping_cart_page.py# Gerencia interações na página do carrinho
|-- tests/                   # Testes organizados por cenário
    |-- using_go_to_cart_button/  # Testes para o botão "Go to Cart"
    |-- using_remove_1_button/    # Testes para remoção de itens
    |-- using_shopping_cart_button/ # Testes para o botão "Shopping Cart"
```

## Pré-requisitos

1. Python 3.8 ou superior instalado.
2. Google Chrome instalado.
3. ChromeDriver compatível com sua versão do Chrome.
4. Instalar dependências do projeto:

```bash
pip install selenium pytest
```

## Padrão de Projeto (POM)

O padrão Page Object Model organiza o código para que a lógica de interação com a interface fique separada dos testes. Isso facilita manutenção e reuso.

- **`base_page.py`**:
  Contém métodos genéricos reutilizáveis, como clicar em elementos ou buscar por eles.

- **Demais arquivos em `pages/`**:
  Cada arquivo representa uma página do site, encapsulando elementos específicos e suas interações.

Exemplo de método em `base_page.py`:

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

## Executando os Testes

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
```

2. Navegue até o diretório do projeto:

```bash
cd selenium-project-pom
```

3. Execute os testes:

```bash
pytest tests/
```

Os resultados serão exibidos no console.

## Estrutura de Testes

Os testes estão organizados por cenário dentro da pasta `tests/`. Cada subpasta representa um fluxo específico:

1. **`using_go_to_cart_button/`**:
   Testa a navegação até o carrinho usando o botão "Go to Cart".

2. **`using_remove_1_button/`**:
   Valida a remoção de itens do carrinho.

3. **`using_shopping_cart_button/`**:
   Testa a navegação ao carrinho usando o botão "Shopping Cart".

Exemplo de um teste:

```python
def test_go_to_cart(driver):
    home_page = HomePage(driver)
    home_page.add_item_to_cart()
    home_page.go_to_cart()

    cart_page = ShoppingCartPage(driver)
    assert cart_page.is_cart_page_displayed()
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.

## Licença

Este projeto está sob a licença MIT.