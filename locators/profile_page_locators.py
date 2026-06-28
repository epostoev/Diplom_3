from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Навигация в личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # Список заказов в истории
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, ".//p[contains(@class,'OrderHistory_number')]")