from enum import Enum
from typing import Pattern
from urllib.parse import urljoin

import allure

from playwright.sync_api import Page, expect

from config import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: Enum):
        full_page_url = urljoin(str(settings.app_url), url.value)
        with allure.step(f'Opening the url "{full_page_url}"'):
            self.page.goto(url.value, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)
