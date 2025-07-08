import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(page):
    page.goto("https://jrnys.com/")
    page.get_by_test_id("login-icon").click()
    page.get_by_test_id("login-email-input").fill("invalidemail@mail.com")
    page.get_by_test_id("login-password-input").fill("password12")
    page.get_by_test_id("login-submit-button").click()

    expect(page.get_by_text("Invalid username or password.", exact=True)).to_be_visible()

