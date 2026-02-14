from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/')
    
    #for css selector id #, class ., attribute tagname[attribute="value"]
  #como usar el id
    emailtxtbox = page.wait_for_selector('#email')
    assert emailtxtbox is not None
    emailtxtbox.fill('test@gmail.com')

    
    buttonsend = page.wait_for_selector('#enterimg')
    assert buttonsend is not None
    buttonsend.click()

    page.wait_for_timeout(3000)