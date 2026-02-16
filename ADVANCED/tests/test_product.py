from playwright.sync_api import Page

def test_add_tocart(login):
    page=login
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click() #busca un button el at asi
    badge=page.locator(".shopping_cart_badge") #cuando se trata de clases se usa .
    assert badge.inner_text() == "1"
    