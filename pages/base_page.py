from enum import Enum
from typing import Pattern
from urllib.parse import urljoin

import allure

from playwright.sync_api import Page, expect
from tools import logger

from config import settings

logger = logger.get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: Enum):
        step = f'Opening the url "{urljoin(str(settings.app_url), url.value)}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url.value, wait_until='networkidle')

    def reload(self):
        step = f'Reloading page with url "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
