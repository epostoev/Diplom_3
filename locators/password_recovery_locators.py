from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    # Страница forgot-password
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    # Страница reset-password
    NEW_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Введите новый пароль']")
    SHOW_HIDE_PASSWORD_BUTTON = (
        By.XPATH,
        ".//div[contains(@class,'input__icon input__icon-action')]"
    )
    PASSWORD_INPUT_CONTAINER = (
        By.XPATH,
        ".//div[contains(@class,'input_type_password')]"
    )
    # Поле пароля подсвечивается классом input_status_active
    PASSWORD_INPUT_ACTIVE = (
        By.XPATH,
        ".//div[contains(@class,'input_status_active')]//input[@name='Введите новый пароль']"
    )