import allure
from selenium.webdriver.support.wait import WebDriverWait

from data import URLS
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем страницу логина")
    def open(self):
        self.go_to_url(URLS.LOGIN_URL)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self):
        # JS-клик обходит Modal_modal_overlay, который перекрывает кнопку в
        # Firefox
        self.click_to_element_js(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Логинимся как {email}")
    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        # Ждём пока URL перестанет содержать /login — значит редирект прошёл
        WebDriverWait(self.driver, 15).until(
            lambda d: "/login" not in d.current_url
        )

    @allure.step("Кликаем на 'Восстановить пароль'")
    def click_forgot_password(self):
        # JS-клик обходит Modal_modal_overlay в Firefox
        self.click_to_element_js(LoginPageLocators.FORGOT_PASSWORD_LINK)
