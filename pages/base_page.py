import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    # def wait_for_element_invisible(self, locator, timeout=5):
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.invisibility_of_element_located(locator)
    #     )
    
    def wait_for_element_invisible(self, locator, timeout=5):
        """Ожидает, пока элемент исчезнет из DOM или станет невидимым."""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def click_to_element_js(self, locator):
        """Кликает по элементу с помощью JavaScript (игнорирует оверлеи)."""
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Прокручиваем страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ждём редирект на URL содержащий: {url_part}")
    def wait_for_url_contains(self, url_part, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    def wait_for_element_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_invisible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def is_element_visible(self, locator):
        try:
            self.wait_for_element_visible(locator, timeout=5)
            return True
        except Exception:
            return False

    def get_element_attribute(self, locator, attribute):
        return self.find_element_with_wait(locator).get_attribute(attribute)

    @allure.step("Ждём открытия новой вкладки")
    def wait_for_new_window(self, expected_count):
        WebDriverWait(self.driver, 10).until(
            EC.number_of_windows_to_be(expected_count)
        )

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1])

    def format_locator(self, locator, value):
        method, xpath = locator
        return method, xpath.format(value)