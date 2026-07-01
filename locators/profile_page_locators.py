from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Навигация в личном кабинете
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # Номер заказа в истории — формат #011230
    ORDER_NUMBER_IN_HISTORY = (
        By.XPATH,
        ".//p[contains(@class,'text_type_digits-default')]"
    )
