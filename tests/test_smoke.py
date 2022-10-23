"""
Базовые тесты
"""
from tests.helper.base_app import BasePage
from selenium.webdriver.common.by import By


def test_get_url(browser):
    """
    Получение URLа
    """
    page = BasePage(browser)
    page.go_to_site()

    assert True, 'Неожиданное состояние'


def test_email(browser):
    """
    Проверка email
    """
    page = BasePage(browser)
    page.go_to_site()

    assert page.get_email() == "e-mail", 'Неожиданный email'


def test_accordion(browser):
    """
    Проверка аккордеона
    """
    page = BasePage(browser)
    page.go_to_site()
    browser.find_element(By.XPATH, value='//*[@id="headingTwo"]/button').click()
    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='collapseTwo'] a")

    assert elements[-1].accessible_name == "Программа для выборки случайной музыки из коллекции", 'Неожиданная ссылка'
