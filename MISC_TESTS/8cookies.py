from playwright.sync_api import sync_playwright

import json

with sync_playwright ()as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    
    page.goto("https://www.redbus.in/")
    mycookies=page.context.cookies()
   # Format the Python dictionary as a JSON string with 4 spaces of indentation
    json_string = json.dumps(mycookies, indent=4)

    # Print the resulting JSON string to the console
    print(json_string)
    
    page.context.clear_cookies()
    new_cookie = {
    "name": "ariel",
    "value": "s45kk5jkkj34k5j34j5",
    "domain": ".redbus.in",
    "path": "/"
}
    page.context.add_cookies([new_cookie])  # type: ignore[arg-type]

# Taking screenshot
    page.screenshot(path='test.png',full_page=True)


    