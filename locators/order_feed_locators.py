from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Список заказов
    ORDER_ITEM = (By.XPATH, ".//*[contains(@class,'OrderHistory_link')]")
    ORDER_NUMBER_IN_FEED = (By.XPATH, ".//*[contains(@class,'OrderHistory_link')]//p[contains(@class,'digits')]")

    # Модальное окно заказа
    ORDER_MODAL_TITLE = (By.XPATH, ".//*[text()='Cостав']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class,'Modal_modal__close')]")

    # Счётчики
    DONE_ALL_TIME_COUNTER = (
        By.XPATH,
        ".//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]"
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