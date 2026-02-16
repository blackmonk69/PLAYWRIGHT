import pytest
from playwright.sync_api import Page

def test_login_success(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role('textbox',name='Username').fill('standard_user')
    page.fill("input[data-test='password']",'secret_sauce')  #este metodo es por atributo
    page.click('input[data-test="login-button"]')
    assert page.url=="https://www.saucedemo.com/inventory.html"
    page.wait_for_timeout(1000)
    
    
def test_login_failure(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder('Username').fill('dsf') #este metodo es el placeholder
    page.fill('#password','sdfa') #este metodo es por id
    page.get_by_text("Login").click()  #este metodo es por contenido de texto
    error_message=page.locator('H3[data-test="error"]').inner_text()
    assert "Epic sadface" in error_message 
    page.wait_for_timeout(1000)
    
    