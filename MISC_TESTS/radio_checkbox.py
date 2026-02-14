from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    
    radio=page.query_selector('//input[@value="FeMale"]')
    radio.click()  #tambien se puede usar radio.click() 
    #hay que hacer una comprobacion de que esta checked
    
    if radio.is_checked():
        print("Passed")
    else :
        print ("Failed")
        
    
    check=page.query_selector('//input[@value="Cricket"]')
    check.check()
   
    page.wait_for_timeout(3000)
    
    #de esta forma se lo busque y selecciona en un solo paso
    #page.select_option('//select[@id="Skills"]',label='Autocad')
    