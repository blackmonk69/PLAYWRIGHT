from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    broswer = p.chromium.launch()
    context = broswer.new_context()
    page = context.new_page()
    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
    # 1. Definir el locator de la tabla
    table = page.locator('//table[@id="customers"]')

    # 2. Obtener todas las filas (tr) usando locators
    tr = table.locator('tr').all() 
    print(len(tr))

    # 3. Obtener todas las celdas (td)
    td = table.locator('td').all()
    print(len(td))
    
    print(len(td))



    for row in tr:
        cells = row.locator('td').all()
        for cell in cells:
            print(cell.text_content())

    page.wait_for_timeout(2000)