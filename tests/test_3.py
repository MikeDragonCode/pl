import pytest
from playwright.sync_api import expect

def test_3(page):
    page.goto("https://demoqa.com/automation-practice-form")

    # Удаляем рекламу
    page.evaluate("document.getElementById('fixedban')?.remove()")
    page.evaluate("document.querySelector('iframe')?.remove()")

    # Заполнение формы
    page.locator("#firstName").fill("John")
    page.locator("#lastName").fill("Doe")
    page.locator("label[for='gender-radio-1']").click()
    page.locator("#userNumber").fill("1234567890")

    # Дата рождения
    page.locator("#dateOfBirthInput").click()
    page.locator(".react-datepicker__year-select").select_option("1990")
    page.locator(".react-datepicker__month-select").select_option("0")
    page.locator(".react-datepicker__day--001:not(.react-datepicker__day--outside-month)").click()

    # Subject
    page.locator("#subjectsInput").fill("Maths")
    page.keyboard.press("Enter")

    # Hobby
    page.locator("label[for='hobbies-checkbox-1']").click()

    # Адрес
    page.locator("#currentAddress").fill("Tbilisi")

    # State & City
    page.locator("#state").click()
    page.get_by_text("NCR", exact=True).click()
    page.locator("#city").click()
    page.get_by_text("Delhi", exact=True).click()

