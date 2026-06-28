from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Список заказов
    ORDER_ITEM = (By.XPATH, ".//a[contains(@class,'OrderFeed_link')]")
    ORDER_NUMBER_IN_FEED = (By.XPATH, ".//p[contains(@class,'OrderFeed_number')]")

    # Модальное окно заказа
    ORDER_MODAL_TITLE = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]//h2[contains(@class,'Modal_modal__title')]"
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]"
        "//button[contains(@class,'Modal_modal__close')]"
    )

    # Счётчики выполненных заказов
    DONE_ALL_TIME_COUNTER = (
        By.XPATH,
        ".//p[text()='Выполнено за всё время:']/following-sibling::p[contains(@class,'OrderFeed_number')]"
    )
    DONE_TODAY_COUNTER = (
        By.XPATH,
        ".//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]"
    )

    # Раздел «В работе»
    IN_PROGRESS_ORDER_NUMBER = (
        By.XPATH,
        ".//ul[contains(@class,'OrderFeed_orderListReady')]//li"
    )