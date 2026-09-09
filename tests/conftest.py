import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()  # это для наглядности, браузер будет и так закрываться при выходе из контекста
