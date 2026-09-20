import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(autouse=True) # autouse - фикстура будет запускаться перед каждым тестом
def test_analytics_data():
    print('[AUTOUSE] Отправляем данные в сервис аналитики')

@pytest.fixture(scope="session")
def settings():
    print('[SESSION] Инициализируем настройки автотестов')

@pytest.fixture(scope="class")
def user():
    print('[CLASS] Созадем данные пользователя один раз на тестовый класс')

@pytest.fixture(scope="function") # function - фикстура по умолчанию
def browser():
    print('[FUNCTION] Открываем браузер на каждый автотест')


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...


# Определение фикстуры
@pytest.fixture
def sample_fixture():
    return {"key": "123"}

# Использование фикстуры в тесте
def test_using_fixture(sample_fixture):
    assert sample_fixture["key"] == "value"


@pytest.fixture
def chromium():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page() # Открываем новое окно браузера
        yield page
        print('returned')# Закрываем окно браузера (teardown)

def test_user_open_page(chromium): # Внутри автотеста уже работает с готовым объектом браузера
    chromium.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Подготовка — данный код будет выполнен до начала автотеста
    resource = "some resource"
    print("!!!Teardown: подготовка ресурса!!!")
    yield resource # Выполняется автотест
    # Очистка — данный код будет выполнен после завершения автотеста
    print("!!!Teardown: освобождение ресурса!!!")

@pytest.fixture
def setup_teardown():
    # Это часть Setup — код, который выполняется перед тестом
    print("Setup: Инициализация данных или окружения")
    test_data = {"user": "testuser", "password": "testpass"}

    # Это часть Teardown — код, который выполняется после теста
    yield test_data  # Здесь возвращаем данные для теста

    print("Teardown: Очистка данных или окружения")
    # Здесь можно закрыть соединения, удалить временные файлы и т.д.
    # Например, удалить созданные записи в базе данных, если таковые были.

def test_login(setup_teardown):
    # Здесь setup_teardown будет содержать возвращённые данные из фикстуры
    assert setup_teardown["user"] == "234"
    assert setup_teardown["password"] == "testpass"