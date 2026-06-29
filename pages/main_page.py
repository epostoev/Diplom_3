import allure
from selenium.webdriver.common.action_chains import ActionChains

from data import URLS
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переходим на главную страницу")
    def open(self):
        self.go_to_url(URLS.BASE_URL)
        # Ждём загрузки ингредиентов
        self.wait_for_element_visible(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Кликаем на ссылку 'Конструктор'")
    def click_constructor_link(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Кликаем на ссылку 'Лента Заказов'")
    def click_order_feed_link(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Кликаем на 'Личный кабинет'")
    def click_profile_link(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(MainPageLocators.PROFILE_LINK)

    @allure.step("Кликаем на первый ингредиент")
    def click_first_ingredient(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверяем что модальное окно ингредиента открылось")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_OPENED)

    @allure.step("Проверяем что заголовок 'Детали ингредиента' виден")
    def is_ingredient_modal_title_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрываем модальное окно крестиком")
    def close_modal(self):
        self.click_to_element_js(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверяем что модальное окно закрылось")
    def is_modal_closed(self):
        return self.wait_for_element_invisible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Получаем значение счётчика первого ингредиента")
    def get_ingredient_counter(self):
        try:
            counter = self.find_element_with_wait(MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except Exception:
            return 0

    @allure.step("Добавляем первый ингредиент в конструктор (drag & drop)")
    def add_first_ingredient_to_constructor(self):
        self.wait_for_overlay_to_disappear()
        ingredient = self.driver.find_element(*MainPageLocators.FIRST_INGREDIENT)
        drop_zone = self.driver.find_element(*MainPageLocators.CONSTRUCTOR_DROP_ZONE)
        ActionChains(self.driver)\
            .click_and_hold(ingredient)\
            .pause(1)\
            .move_to_element(drop_zone)\
            .pause(1)\
            .release()\
            .perform()

    @allure.step("Нажимаем 'Оформить заказ'")
    def click_place_order(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получаем номер заказа из модального окна")
    def get_order_number_from_modal(self):
        element = self.wait_for_element_visible(MainPageLocators.ORDER_ID_IN_MODAL, timeout=30)
        return element.text

    @allure.step("Закрываем модальное окно заказа")
    def close_order_modal(self):
        self.click_to_element_js(MainPageLocators.MODAL_CLOSE_BUTTON)