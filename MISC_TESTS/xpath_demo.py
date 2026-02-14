from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    
    #xpath =relative xpath es con //
    # using attribute //tagname[@attributename="value"]
    
    page.locator('input[name="username"]').fill('admin')
    page.locator('input[placeholder="Password"]').fill('admin123')
    page.locator('button[type="submit"]').click()

    
    page.wait_for_timeout(3000)