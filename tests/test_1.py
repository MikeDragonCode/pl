from playwright.sync_api import sync_playwright, expect

def test_run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://jrnys.com/")
        page.get_by_test_id("login-icon").click()
        page.get_by_test_id("login-email-input").fill("invalidemail@mail.com")
        page.get_by_test_id("login-password-input").fill("password12")
        page.get_by_test_id("login-submit-button").click()

        expect(page.get_by_text("Invalid username or password.", exact=True)).to_be_visible()

        context.close()
        browser.close()