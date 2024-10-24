#Импортируем Пай тест
import  pytest

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