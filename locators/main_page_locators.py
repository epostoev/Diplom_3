from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[contains(text(), 'Конструктор')]/..")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/..")
    PROFILE_LINK = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]/..")

    # Первый ингредиент в списке
    FIRST_INGREDIENT = (
        By.XPATH,
        "(.//a[contains(@class,'BurgerIngredient_ingredient')])[1]")

    # Счётчик на первом ингредиенте
    INGREDIENT_COUNTER = (
        By.XPATH,
        "(.//a[contains(@class,'BurgerIngredient_ingredient')])[1]"
        "//p[contains(@class,'counter_counter__num')]"
    )

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]")
    INGREDIENT_MODAL_TITLE = (
        By.XPATH, ".//h2[contains(text(),'Детали ингредиента')]")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        ".//button[contains(@class,'Modal_modal__close')]"
    )

    # Кнопка оформить заказ
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        ".//button[contains(@class,'button_button__33qZ0') and text()='Оформить заказ']"
    )

    # Модальное окно с номером заказа
    ORDER_ID_IN_MODAL = (
        By.XPATH,
        ".//h2[contains(@class,'Modal_modal__title')]")

    # Корзина конструктора
    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        ".//ul[contains(@class,'BurgerConstructor_basket__list')]"
    )

    # Открытая модалка (класс меняется при открытии)
    INGREDIENT_MODAL_OPENED = (
        By.XPATH, ".//section[contains(@class,'Modal_modal_opened')]")
