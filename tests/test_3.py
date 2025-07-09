import pytest
from playwright.sync_api import expect

def test_3(page):
    page.goto("https://demoqa.com/automation-practice-form")

    # Удаляем рекламный баннер, который мешает кликать
    page.evaluate("document.getElementById('fixedban')?.remove()")
    page.evaluate("document.querySelector('iframe')?.remove()")

    page.get_by_label("First Name").fill("John")
    page.get_by_label("Last Name").fill("Doe")
    page.get_by_label("Email").fill("john.doe@example.com")
    page.get_by_label("Male").click()
    page.get_by_label("Mobile Number").fill("1234567890")

    expect(page.get_by_text("Thanks for submitting the form")).not_to_be_visible()