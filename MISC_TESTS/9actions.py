from playwright.sync_api import sync_playwright

with sync_playwright ()as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    page.get_by_role("link", name="SwitchTo").hover()
    
    page.get_by_role("link", name="SwitchTo").click()
    
    page.get_by_role("link", name="SwitchTo").dblclick()
    
    page.get_by_role("link", name="SwitchTo").click(button='right')
    
    #hace click con shift
    page.get_by_role("link", name="SwitchTo").click(modifiers=["Shift"])
    
    page.get_by_role("link", name="SwitchTo").press ("A")
    page.wait_for_timeout(3000)

    