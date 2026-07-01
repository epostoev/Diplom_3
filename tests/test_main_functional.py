import allure

from data import URLS
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход в Конструктор по клику на ссылку 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        # Сначала уходим на ленту заказов, потом возвращаемся через навигацию
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        main_page = MainPage(driver)
        main_page.click_constructor_link()
        main_page.wait_for_url_contains(URLS.BASE_URL)
        assert main_page.get_current_url() == URLS.BASE_URL

    @allure.title("Переход в 'Ленту Заказов' по клику на ссылку")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed_link()
        main_page.wait_for_url_contains(URLS.ORDER_FEED_URL)
        assert URLS.ORDER_FEED_URL in main_page.get_current_url()

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_visible(), \
            "Модальное окно с деталями ингредиента не появилось"

    @allure.title("Всплывающее окно ингредиента закрывается кликом по крестику")
    def test_close_ingredient_modal_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_closed(), \
            "Модальное окно не закрылось после клика по крестику"

    @allure.title("При добавлении ингредиента в заказ увеличивается счётчик")
    def test_ingredient_counter_increases_on_add(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        counter_before = main_page.get_ingredient_counter()
        main_page.add_first_ingredient_to_constructor()
        counter_after = main_page.get_ingredient_counter()
        assert counter_after > counter_before, \
            f"Счётчик не увеличился: было {counter_before}, стало {counter_after}"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.open()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_place_order()
        order_number = main_page.get_order_number_from_modal()
        assert order_number.isdigit(), \
            f"Номер заказа не получен или не является числом: '{order_number}'"
