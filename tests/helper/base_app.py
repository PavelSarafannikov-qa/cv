"""
Объект страницы
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Объект страницы
    """
    LOCATOR_EMAIL = (By.CSS_SELECTOR, '[class="nav-link fw-bold py-1 px-0"]')

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://nuu-vot.github.io"

    def find_element(self, locator, time=10):
        """
        Поиск элемента с ожиданием
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент по локатору {locator}")

    def go_to_site(self):
        """
        Переход на сайт
        """
        return self.driver.get(self.base_url)

    def get_email(self):
        """
        Get email from page
        """
        _el = self.find_element(self.LOCATOR_EMAIL, time=2)
        return _el.text
