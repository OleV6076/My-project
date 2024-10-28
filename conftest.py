#Импортируем
import  pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


#Функция pytest_addoption добавляет новый параметр командной строки для pytest
def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language: en or fr or ru etc."
    )

#декоратор, указывающий, что данная фикстура будет создана и уничтожена для каждой тестовой функции отдельно
@pytest.fixture(scope="function")
def browser_language(request):
    language = request.config.getoption("language")
    return language

#Фикстура позволяет удобно инициализировать и закрывать браузер для каждого теста
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()
