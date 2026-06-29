import allure

from data import URLS
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в личный кабинет по клику на 'Личный кабинет'")
    def test_navigate_to_profile(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.click_profile_link()
        main_page.wait_for_url_contains(URLS.PROFILE_URL)
        assert URLS.PROFILE_URL in logged_in_driver.current_url

    @allure.title("Переход в 'История заказов' из личного кабинета")
    def test_navigate_to_order_history(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        profile_page.open()
        profile_page.click_order_history()
        profile_page.wait_for_url_contains(URLS.ORDER_HISTORY_URL)
        assert URLS.ORDER_HISTORY_URL in logged_in_driver.current_url

    @allure.title("Выход из аккаунта через личный кабинет")
    def test_logout(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        profile_page.open()
        profile_page.click_logout()
        profile_page.wait_for_url_contains(URLS.LOGIN_URL)
        assert URLS.LOGIN_URL in logged_in_driver.current_url
