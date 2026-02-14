from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    
    select_dropdown = page.wait_for_selector('#Skills')
    assert select_dropdown is not None
    select_dropdown.select_option(label='Art Design')
    
    page.wait_for_timeout(2000)
    
    #de esta forma se lo busque y selecciona en un solo paso
    page.locator('#Skills').select_option(label='AutoCAD')
    page.wait_for_timeout(2000)

    