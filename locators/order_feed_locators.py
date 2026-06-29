from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Карточка заказа в ленте
    ORDER_ITEM = (By.XPATH, ".//*[contains(@class,'OrderHistory_link')]")

    # Номер заказа в карточке ленты
    ORDER_NUMBER_IN_FEED = (
        By.XPATH,
        ".//*[contains(@class,'OrderHistory_link')]//p[contains(@class,'text_type_digits-default')]"
    )

    # Модальное окно заказа — ищем по тексту «Cостав» внутри открытой модалки
    ORDER_MODAL_TITLE = (By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class,'Modal_modal__close')]")

    # Счётчики — первый «за всё время», второй «за сегодня»
    DONE_ALL_TIME_COUNTER = (
        By.XPATH,
        "(.//p[contains(@class,'OrderFeed_number')])[1]"
    )
    DONE_TODAY_COUNTER = (
        By.XPATH,
        "(.//p[contains(@class,'OrderFeed_number')])[2]"
    )

    # Раздел «В работе» — li с номерами заказов
    IN_PROGRESS_ORDER_NUMBER = (
        By.XPATH,
        ".//ul[contains(@class,'OrderFeed_orderList')]"
        "//li[contains(@class,'text_type_digits-default')]"
    )