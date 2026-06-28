import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from data import URLS, UserData
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage
from pages.password_recovery_page import PasswordRecoveryPage


# Кроссбраузерность: фикстура запускается дважды — в Chrome и Firefox
@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    if request.param == "Chrome":
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    browser.maximize_window()
    browser.get(URLS.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def registered_user():
    """Создаём пользователя через API перед тестом, удаляем после."""
    payload = {
        "email": UserData.EMAIL,
        "password": UserData.PASSWORD,
        "name": UserData.NAME
    }

    # Если пользователь уже существует — логинимся и удаляем, чтобы не было конфликта
    login_resp = requests.post(URLS.LOGIN_API_URL, json={
        "email": UserData.EMAIL,
        "password": UserData.PASSWORD
    })
    if login_resp.status_code == 200:
        old_token = login_resp.json().get("accessToken")
        requests.delete(URLS.USER_URL, headers={"Authorization": old_token})

    resp = requests.post(URLS.REGISTER_URL, json=payload)
    assert resp.status_code == 200, f"Не удалось создать пользователя: {resp.text}"
    token = resp.json().get("accessToken")

    yield {"email": UserData.EMAIL, "password": UserData.PASSWORD, "token": token}

    # Удаляем пользователя после теста
    if token:
        requests.delete(
            URLS.USER_URL,
            headers={"Authorization": token}
        )


@pytest.fixture
def logged_in_driver(driver, registered_user):
    """Драйвер с уже залогиненным пользователем."""
    login_page = LoginPage(driver)
    login_page.login(registered_user["email"], registered_user["password"])
    return driver


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def profile_page(logged_in_driver):
    return ProfilePage(logged_in_driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)