from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EBAY_EMAIL")
PASSWORD = os.getenv("EBAY_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://signin.ebay.com/")

    page.fill('input#userid', EMAIL)
    page.click('button#signin-continue-btn')

    page.wait_for_selector('input#pass')
    page.fill('input#pass', PASSWORD)
    page.click('button#sgnBt')

    page.wait_for_selector("button[aria-label*='My eBay']")

    context.storage_state(path="auth.json")
    browser.close()
    print("✅ Сессия сохранена в auth.json")