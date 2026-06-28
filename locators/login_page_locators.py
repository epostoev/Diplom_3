from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text' and @name='name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")