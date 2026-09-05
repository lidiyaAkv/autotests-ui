from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_form_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_form_email_input).to_be_visible()

    login_form_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_form_password_input).to_be_visible()

    login_page_login_button = page.get_by_test_id('login-page-login-button')
    expect(login_page_login_button).to_be_visible()

    login_page_registration_link = page.get_by_test_id('login-page-registration-link')
    login_page_registration_link.click()

    registration_form_email_input = page.locator('div[data-testid="registration-form-email-input"] input')
    expect(registration_form_email_input).to_be_visible()

    registration_form_password_input = page.locator('div[data-testid="registration-form-password-input"] input')
    expect(registration_form_password_input).to_be_visible()

    registration_page_registration_button = page.locator('button#registration-page-registration-button')
    expect(registration_page_registration_button).to_be_visible()

    page.wait_for_timeout(2500)