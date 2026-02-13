from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    
    #for css selector id #, class ., attribute tagname[attribute="value"]
  #como usar el id
    username=page.wait_for_selector('input[name="username"]')
    username.type('Admin')
    
    username=page.wait_for_selector('input[type="password"]')
    username.type('admin123')
    
    botonlogin=page.wait_for_selector('button[type="submit"]')
    
    botonlogin.click()
    page.wait_for_timeout(3000)