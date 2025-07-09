from playwright.sync_api import sync_playwright, expect

def test_run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://jrnys.com/")
        page.get_by_test_id("login-icon").click()
        page.get_by_test_id("login-email-input").fill("invalid1")
        page.get_by_test_id("login-submit-button").click()

        expect(page.get_by_test_id("login-email-error-message")).to_have_text("Value is not a valid email address")

        context.close()
        browser.close()