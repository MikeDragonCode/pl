def test_login_success(page):
    page.goto("https://www.ebay.com/")
    page.click("text=My eBay")
    page.click("text=Purchase History")
    page.fill("input[name='Search your orders']", "jordan")
    page.click("text=Search")
    page.wait_for_selector("text=token", timeout=5000)