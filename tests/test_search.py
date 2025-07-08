import re
import pytest
from playwright.sync_api import Page, expect


def test_navigate_to_basespace_sequence_hub(page: Page):
    page.goto("https://www.illumina.com/")

    # Закрытие всплывающих окон (если есть)
    try:
        page.get_by_role("button", name="Got it").click(timeout=3000)
    except:
        pass
    try:
        page.locator("#ilmn-modal").get_by_label("Close").click(timeout=3000)
    except:
        pass

    # Наведение на Products → Software & Analysis
    page.get_by_role("button", name="Products").hover()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Software & Analysis").hover()
    page.wait_for_timeout(500)

    # Переход на BaseSpace Sequence Hub
    link = page.get_by_role("link", name="BaseSpace Sequence Hub").nth(0)
    expect(link).to_be_visible()
    link.click()

    # Проверка URL
    expect(page).to_have_url(re.compile(".*basespace.*", re.IGNORECASE))

