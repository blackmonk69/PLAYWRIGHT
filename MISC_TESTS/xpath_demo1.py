from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    
    #xpath =relative xpath es con //
    # using attribute //tagname[@attributename="value"]
    # USAMOS LA BUSQUEDA CON UN TEXTO
    # text //tagname[text()="text"]
    # text - //tagname[text()="text"]
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    page.wait_for_timeout(3000)
    
    # contains
# attributes - //tagname[contains(@attribute,"value")]
# //input[contains(@placeholder,"User")]
# text - //tagname[contains(text(),"Forgot your")]
# // label[contains(text(), "Username")]

# dynamic - prasanth123,prasanth13454,prasanth987
# starts-with - //tagname[starts-with(@id,'prasanth')]
# ends-with - 2343user

# family
# parent - //tagname[@id = "xy"]/parent::input[]
# child - //tagname[@id = "xy"]/child::input[]
# ancestor - 
# sibling - //td[text()="Microsoft"]//following-sibling::td[2]