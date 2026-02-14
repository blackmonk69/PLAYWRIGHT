from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    
    page.locator('input[value="FeMale"]').check()
 
    
    radio = page.locator('input[value="FeMale"]')

    if radio.is_checked():
        print("Passed")
    else:
        print("Failed")
        
    
    page.locator('input[value="Cricket"]').check()

   
    page.wait_for_timeout(3000)
    
    #de esta forma se lo busque y selecciona en un solo paso
    #page.select_option('//select[@id="Skills"]',label='Autocad')
    