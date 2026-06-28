from selenium.webdriver.common.by import By


class MainPageLocators:
    # Навигация в шапке
    CONSTRUCTOR_LINK = (By.XPATH, ".//a[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, ".//a[text()='Лента заказов']")
    PROFILE_LINK = (By.XPATH, ".//a[contains(@href, '/account')]")

    # Конструктор — секции
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']")

    # Первый ингредиент в списке (булка)
    FIRST_INGREDIENT = (By.XPATH, "(.//a[contains(@class,'BurgerIngredient_ingredient')])[1]")

    # Счётчик на ингредиенте
    INGREDIENT_COUNTER = (
        By.XPATH,
        "(.//a[contains(@class,'BurgerIngredient_ingredient')])[1]//"
        "p[contains(@class,'counter_counter__num')]"
    )

    # Модальное окно ингредиента
    INGREDIENT_MODAL = (By.XPATH, ".//section[contains(@class,'Modal_modal__container')]")
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]//h3[text()='Детали ингредиента']"
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]"
        "//button[contains(@class,'Modal_modal__close')]"
    )

    # Кнопка оформить заказ
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        ".//button[contains(@class,'Button_button') and text()='Оформить заказ']"
    )

    # Модальное окно с номером заказа
    ORDER_ID_IN_MODAL = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]//h2[contains(@class,'Modal_modal__title')]"
    )
    ORDER_MODAL_CLOSE = (
        By.XPATH,
        ".//section[contains(@class,'Modal_modal__container')]"
        "//button[contains(@class,'Modal_modal__close')]"
    )

    # Корзина конструктора
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor_basket__list')]")