import allure

from data import URLS
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.main_page_locators import MainPageLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открываем ленту заказов")
    def open(self):
        # go_to_url безопасен здесь — страница /feed публичная, не требует авторизации
        self.go_to_url(URLS.ORDER_FEED_URL)
        self.wait_for_element_visible(OrderFeedLocators.ORDER_ITEM)

    @allure.step("Открываем ленту заказов через навигацию (сохраняет localStorage)")
    def open_via_nav(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(MainPageLocators.ORDER_FEED_LINK)
        self.wait_for_url_contains(URLS.ORDER_FEED_URL)
        self.wait_for_element_visible(OrderFeedLocators.ORDER_ITEM)

    @allure.step("Кликаем на первый заказ в ленте")
    def click_first_order(self):
        self.wait_for_overlay_to_disappear()
        self.click_to_element_js(OrderFeedLocators.ORDER_ITEM)

    @allure.step("Проверяем что модальное окно заказа открылось")
    def is_order_modal_visible(self):
        return self.is_element_visible(OrderFeedLocators.ORDER_MODAL_TITLE)

    @allure.step("Закрываем модальное окно заказа")
    def close_order_modal(self):
        self.click_to_element_js(OrderFeedLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получаем счётчик 'Выполнено за всё время'")
    def get_done_all_time_count(self):
        return int(self.get_text_from_element(OrderFeedLocators.DONE_ALL_TIME_COUNTER))

    @allure.step("Получаем счётчик 'Выполнено за сегодня'")
    def get_done_today_count(self):
        return int(self.get_text_from_element(OrderFeedLocators.DONE_TODAY_COUNTER))

    @allure.step("Получаем список номеров заказов в ленте")
    def get_order_numbers_in_feed(self):
        elements = self.find_elements_with_wait(OrderFeedLocators.ORDER_NUMBER_IN_FEED)
        return [el.text for el in elements]

    @allure.step("Получаем список заказов в разделе 'В работе'")
    def get_in_progress_order_numbers(self):
        try:
            elements = self.find_elements_with_wait(OrderFeedLocators.IN_PROGRESS_ORDER_NUMBER)
            return [el.text for el in elements]
        except Exception:
            return []