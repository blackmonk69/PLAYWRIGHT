from playwright.sync_api import sync_playwright

with sync_playwright ()as p:
    
    try:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')
    
        page.query_selector_all('d//[@sf="werf"]').click()
        
        #guarda todos los links de una pagina en elements
        
        elements=page.query_selector_all("a")
        print(len(elements))
        for i in elements:
            print(i.get_attribute("href"))
        page.wait_for_timeout(1000)
    except Exception as e:
        print(str(e))
    finally:
        print("Execute")
        
        
          
        
        