import allure

from data import URLS
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу восстановления пароля")
    def open(self):
        self.go_to_url(URLS.FORGOT_PASSWORD_URL)

    @allure.step("Вводим email для восстановления")
    def enter_email(self, email):
        self.add_text_to_element(PasswordRecoveryLocators.EMAIL_INPUT, email)

    @allure.step("Нажимаем кнопку 'Восстановить'")
    def click_recover_button(self):
        # self.click_to_element(PasswordRecoveryLocators.RECOVER_BUTTON)
        self.click_to_element_js(PasswordRecoveryLocators.RECOVER_BUTTON)

    @allure.step("Нажимаем кнопку показать/скрыть пароль")
    def click_show_hide_password(self):
        self.click_to_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step("Проверяем, что поле пароля стало активным (подсвечено)")
    def is_password_field_active(self):
        return self.is_element_visible(PasswordRecoveryLocators.PASSWORD_INPUT_ACTIVE)