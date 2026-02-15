from playwright.sync_api import sync_playwright


def download_handle(download):
    location_file = './files/test.zip'
    download.save_as(location_file)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/FileDownload.html')
    page.on('download', download_handle)
    
   # En lugar de solo esperar un tiempo arbitrario, 
    # capturamos la promesa de la descarga
    with page.expect_download() as download_info:
        page.locator('//a[@href="https://github.com//sakinala/AutomationTesting/raw/master/samplefile.pdf"]').click()
    
    page.wait_for_timeout(2000)