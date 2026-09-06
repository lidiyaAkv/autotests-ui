from playwright.sync_api import sync_playwright, Request, Response
from http import HTTPStatus

def log_request(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    status = response.status
    text = HTTPStatus(status).phrase
    print(f'Response: {response.url} {status} {text}')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request) # добавили обработчик на событие request
    # page.remove_listener('request', log_request) # убрали обработчик на событие request
    page.on('response', log_response)

    page.wait_for_timeout(2500)