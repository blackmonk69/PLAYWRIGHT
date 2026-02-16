from playwright.sync_api import Page

def test_add_tocart(login):
    page=login
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click() #busca un button el at asi
    badge=page.locator(".shopping_cart_badge") #cuando se trata de clases se usa .
    texto=badge.inner_text()
    page.wait_for_timeout(2000)
    assert badge.inner_text() == "1"
    
def test_product_titles_visible(login):
    page = login
    titles = page.locator(".inventory_item_name")  #es una clase, por eso el punto
    
    assert titles.count() > 0