# Файлы для линтера — можно переключать комментарием
# FILE_1 = $(shell find ./tests -name "*.py" -type f)
# FILE_1 = $(shell find ./pages -name "*.py" -type f)
# FILE_1 = $(shell find ./locators -name "*.py" -type f)
# FILE_1 = data.py
# FILE_1 = conftest.py

lint:
	python3 -m flake8 $(FILE_1)

fix:
	python3 -m autopep8 --in-place --aggressive --aggressive $(FILE_1)

test:
	pytest -v -s --alluredir=allure-results

report:
	allure serve allure-results

test-chrome:
	pytest -v -s -k "Chrome" --alluredir=allure-results

test-firefox:
	pytest -v -s -k "Firefox" --alluredir=allure-results

clean:
	rm -rf allure-results allure-report