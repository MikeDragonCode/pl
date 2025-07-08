import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
def test_3(page):
    page.goto("https://demoqa.com/automation-practice-form")

    page.locator('#firstName').fill('Mike')
    page.locator('#lastName').fill('QA')
    page.locator("label[for='gender-radio-1']").click()
    page.locator('#userNumber').fill('5112115941')

    # Дата рождения
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__year-select').select_option('1990')
    page.locator('.react-datepicker__month-select').select_option('0')
    page.locator(".react-datepicker__day--001:not(.react-datepicker__day--outside-month)").click()

    # Обязательный SUBJECT (важно нажать Enter!)
    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press('Enter')

    # Обязательный HOBBY
    page.locator("label[for='hobbies-checkbox-1']").click()

    # Адрес
    page.locator('#currentAddress').fill('Tbilisi, Rustaveli Ave 10')

    # State and City
    page.locator("#state").click()
    page.get_by_text("NCR", exact=True).click()
    page.locator("#city").click()
    page.get_by_text("Delhi", exact=True).click()

    # Сабмит
    print("Перед сабмитом")
    page.locator('#submit').scroll_into_view_if_needed()
    page.locator('#submit').click(force=True)
    print("После сабмита")

    # Проверка
    expect(page.locator("//td[text()='Student Name']/following-sibling::td")).to_have_text("Mike QA")