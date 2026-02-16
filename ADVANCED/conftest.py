import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from playwright.sync_api import expect


load_dotenv()

USERNAME = os.getenv("SAUCEUSERNAME", "")
PASSWORD = os.getenv("SAUCEPASSWORD", "")


@pytest.fixture  #esto hace que nuestros tests empiezen directamente desde el inventory page, 
def login(page: Page) -> Page:  #fixture prepara el terreno para los tests
    page.goto("https://www.saucedemo.com/")
    page.get_by_role('textbox',name="Username").fill(USERNAME)
    page.fill("input[data-test='password']",PASSWORD)  #este metodo es por atributo  #esto
    page.click('input[data-test="login-button"]') 
    return page

