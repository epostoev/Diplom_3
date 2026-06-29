import time

import allure

from data import URLS
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Клик на заказ в ленте открывает всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open()
        order_feed_page.click_first_order()
        assert order_feed_page.is_order_modal_visible(), \
            "Модальное окно заказа не появилось"

    @allure.title("Заказы из 'Истории заказов' отображаются в 'Ленте заказов'")
    def test_user_orders_visible_in_feed(
            self, logged_in_driver, registered_user):
        # Создаём заказ
        main_page = MainPage(logged_in_driver)
        main_page.open()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_place_order()
        main_page.get_order_number_from_modal()
        main_page.close_order_modal()

        # Смотрим историю заказов
        profile_page = ProfilePage(logged_in_driver)
        profile_page.open()
        profile_page.click_order_history()
        profile_page.wait_for_url_contains(URLS.ORDER_HISTORY_URL)
        history_orders = profile_page.get_order_numbers()

        # Смотрим ленту заказов
        order_feed_page = OrderFeedPage(logged_in_driver)
        order_feed_page.open_via_nav()
        feed_orders = order_feed_page.get_order_numbers_in_feed()

        assert any(o in ' '.join(feed_orders) for o in history_orders), \
            f"Заказы пользователя {history_orders} не найдены в ленте {feed_orders}"

    @allure.title("При создании заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_all_time_counter_increases_after_order(self, logged_in_driver):
        order_feed_page = OrderFeedPage(logged_in_driver)
        order_feed_page.open_via_nav()
        count_before = order_feed_page.get_done_all_time_count()

        main_page = MainPage(logged_in_driver)
        main_page.open()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_place_order()
        main_page.get_order_number_from_modal()
        main_page.close_order_modal()

        order_feed_page.open_via_nav()
        # Ждём пока счётчик обновится
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(logged_in_driver, 15).until(
            lambda d: order_feed_page.get_done_all_time_count() > count_before
        )
        count_after = order_feed_page.get_done_all_time_count()
        assert count_after > count_before, \
            f"Счётчик 'за всё время' не увеличился: было {count_before}, стало {count_after}"

    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_counter_increases_after_order(self, logged_in_driver):
        order_feed_page = OrderFeedPage(logged_in_driver)
        order_feed_page.open_via_nav()
        count_before = order_feed_page.get_done_today_count()

        main_page = MainPage(logged_in_driver)
        main_page.open()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_place_order()
        main_page.get_order_number_from_modal()
        main_page.close_order_modal()

        order_feed_page.open_via_nav()
        # Ждём пока счётчик обновится
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(logged_in_driver, 15).until(
            lambda d: order_feed_page.get_done_today_count() > count_before
        )
        count_after = order_feed_page.get_done_today_count()
        assert count_after > count_before, \
            f"Счётчик 'за сегодня' не увеличился: было {count_before}, стало {count_after}"

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_appears_in_progress(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        main_page.open()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_place_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_order_modal()

        order_feed_page = OrderFeedPage(logged_in_driver)
        order_feed_page.open_via_nav()
        # Ждём появления заказа в «В работе»
        time.sleep(3)
        in_progress = order_feed_page.get_in_progress_order_numbers()
        assert any(order_number in item for item in in_progress), \
            f"Заказ #{order_number} не найден в разделе 'В работе': {in_progress}"
