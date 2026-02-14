from playwright.sync_api import sync_playwright

text_alert=[]
def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

# registrar el handler ANTES
    page.on("dialog", handle_dialog)

    # abrir el tab
    page.locator('a[href="#CancelTab"]').click()

    # click en el botón dentro del tab
    page.locator('#CancelTab button').click()

    page.wait_for_timeout(2000)
    print(text_alert[0])
    