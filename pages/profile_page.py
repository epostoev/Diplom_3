import allure

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем личный кабинет через навигацию")
    def open(self):
        # Переходим через клик на ссылку в хедере, а не через go_to_url,
        # чтобы не потерять localStorage с токеном авторизации
        self.click_to_element_js(MainPageLocators.PROFILE_LINK)
        self.wait_for_url_contains("account")

    @allure.step("Кликаем 'История заказов'")
    def click_order_history(self):
        self.click_to_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Нажимаем кнопку 'Выход'")
    def click_logout(self):
        self.click_to_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Получаем список номеров заказов из истории")
    def get_order_numbers(self):
        elements = self.find_elements_with_wait(
            ProfilePageLocators.ORDER_NUMBER_IN_HISTORY)
        return [el.text for el in elements]
