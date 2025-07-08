import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(page):
    page.goto("https://jrnys.com/")
    page.get_by_test_id("login-icon").click()
    page.get_by_test_id("login-email-input").fill("invalid1")
    page.get_by_test_id("login-submit-button").click()

    expect(page.get_by_test_id("login-email-error-message")).to_have_text("Value is not a valid email address")

