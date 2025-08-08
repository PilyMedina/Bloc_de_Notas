import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
@pytest.fixture(scope="session") 
#abre buscador en grande
def buscador(): 
    options= Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
#este inicia el  buscador
    driver= webdriver.Chrome(service=Service(),options= Options())
    yield driver 
    driver.quit()

    