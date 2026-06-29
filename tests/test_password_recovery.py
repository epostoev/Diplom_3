import allure

from data import URLS, UserData
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password()
        assert URLS.FORGOT_PASSWORD_URL in driver.current_url

    @allure.title("Ввод почты и клик по кнопке 'Восстановить' переводит на страницу сброса пароля")
    def test_enter_email_and_click_recover(self, driver):
        page = PasswordRecoveryPage(driver)
        page.open()
        page.enter_email(UserData.EMAIL)
        page.click_recover_button()
        page.wait_for_url_contains(URLS.RESET_PASSWORD_URL)
        assert URLS.RESET_PASSWORD_URL in driver.current_url

    @allure.title("Клик на показать/скрыть пароль подсвечивает поле ввода")
    def test_show_hide_password_activates_field(self, driver):
        page = PasswordRecoveryPage(driver)
        # Попадаем на страницу reset-password через forgot-password
        page.open()
        page.enter_email(UserData.EMAIL)
        page.click_recover_button()
        page.wait_for_url_contains(URLS.RESET_PASSWORD_URL)
        page.click_show_hide_password()
        assert page.is_password_field_active(
        ), "Поле пароля не стало активным после клика на показать/скрыть"
