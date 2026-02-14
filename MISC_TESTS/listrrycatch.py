from playwright.sync_api import sync_playwright

with sync_playwright ()as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')
   
    #guarda todos los tags b en una lista elements
    
    elements=page.query_selector_all("b")
    print(len(elements))
    for i in elements:
        print(i.text_content())
    page.wait_for_timeout(3000)    
    
    