from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    
    #for css selector id #, class ., attribute tagname[attribute="value"]
  #como usar el id
    username = page.locator('input[name="username"]')
    username.fill("Admin")
    
    
    
    username=page.locator('input[type="password"]')
    username.type('admin123')
    
    botonlogin=page.locator('button[type="submit"]')
    
    botonlogin.click()
    page.wait_for_timeout(3000)