# Diplom_3 — UI-тесты для Stellar Burgers

Автотесты для веб-приложения [Stellar Burgers](https://qa-stellarburgers.education-services.ru/).  
Покрыты сценарии восстановления пароля, личного кабинета, основного функционала конструктора и ленты заказов.

## Список реализованных тестов

### 🔑 Восстановление пароля (`TestPasswordRecovery`)

| Тест | Описание |
|:---|:---|
| `test_navigate_to_forgot_password_page` | Переход на страницу восстановления пароля по кнопке «Восстановить пароль». |
| `test_enter_email_and_click_recover` | Ввод почты и клик по кнопке «Восстановить» переводит на страницу сброса пароля. |
| `test_show_hide_password_activates_field` | Клик на показать/скрыть пароль подсвечивает поле ввода. |

### 👤 Личный кабинет (`TestProfile`)

| Тест | Описание |
|:---|:---|
| `test_navigate_to_profile` | Переход в личный кабинет по клику на «Личный Кабинет». |
| `test_navigate_to_order_history` | Переход в раздел «История заказов» из личного кабинета. |
| `test_logout` | Выход из аккаунта через кнопку «Выход». |

### 🍔 Основной функционал (`TestMainFunctionality`)

| Тест | Описание |
|:---|:---|
| `test_navigate_to_constructor` | Переход в Конструктор по клику на ссылку «Конструктор». |
| `test_navigate_to_order_feed` | Переход в «Ленту Заказов» по клику на ссылку. |
| `test_click_ingredient_opens_modal` | Клик на ингредиент открывает всплывающее окно с деталями. |
| `test_close_ingredient_modal_by_cross` | Всплывающее окно ингредиента закрывается кликом по крестику. |
| `test_ingredient_counter_increases_on_add` | При добавлении ингредиента в заказ увеличивается счётчик. |
| `test_logged_in_user_can_place_order` | Залогиненный пользователь может оформить заказ. |

### 📋 Лента заказов (`TestOrderFeed`)

| Тест | Описание |
|:---|:---|
| `test_click_order_opens_modal` | Клик на заказ в ленте открывает всплывающее окно с деталями. |
| `test_user_orders_visible_in_feed` | Заказы пользователя из «Истории заказов» отображаются в «Ленте заказов». |
| `test_all_time_counter_increases_after_order` | При создании заказа счётчик «Выполнено за всё время» увеличивается. |
| `test_today_counter_increases_after_order` | При создании заказа счётчик «Выполнено за сегодня» увеличивается. |
| `test_new_order_appears_in_progress` | После оформления заказа его номер появляется в разделе «В работе». |

---

## 🛠 Технические особенности реализации

- **Page Object Model** — каждая страница описана отдельным классом в пакете `pages/`. Общие методы вынесены в `BasePage`.
- **Локаторы** — вынесены в отдельный пакет `locators/`, по файлу на каждую страницу.
- **Кроссбраузерность** — тесты запускаются в Chrome и Firefox через параметризованную фикстуру `driver(params=['Chrome', 'Firefox'])`.
- **Allure-отчёты** — каждый тест и класс размечен `@allure.feature`, `@allure.title`, шаги в Page Object — `@allure.step`.
- **Создание тестовых данных через API** — пользователь создаётся через API перед тестом и удаляется после через `yield` (teardown). Защита от дублирования: перед созданием проверяется существование пользователя.
- **JS-клик** — используется для обхода `Modal_modal_overlay`, который в Firefox перекрывает интерактивные элементы.
- **localStorage вместо cookies** — сайт хранит токен в `localStorage`. Навигация между страницами выполняется через клики по ссылкам (SPA-навигация), а не через `driver.get()`, чтобы не потерять сессию.

---

## 🚀 Запуск проекта

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск всех тестов в обоих браузерах
```bash
pytest -v
```

### Запуск с генерацией Allure-отчёта
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### Запуск конкретного файла
```bash
pytest tests/test_profile.py -v
```

---

## 📁 Структура проекта

```
Diplom_3/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── main_page.py
│   ├── order_feed_page.py
│   ├── password_recovery_page.py
│   └── profile_page.py
├── locators/
│   ├── __init__.py
│   ├── login_page_locators.py
│   ├── main_page_locators.py
│   ├── order_feed_locators.py
│   ├── password_recovery_locators.py
│   └── profile_page_locators.py
├── tests/
│   ├── __init__.py
│   ├── test_main_functional.py
│   ├── test_order_feed.py
│   ├── test_password_recovery.py
│   └── test_profile.py
├── conftest.py
├── data.py
├── pytest.ini
└── requirements.txt
```