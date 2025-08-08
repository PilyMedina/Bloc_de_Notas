import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from dotenv import load_dotenv
import os
import time

load_dotenv(dotenv_path=".env")

usuario = os.getenv("correo")
contras = os.getenv("contra")

def test_login_incorrecto(buscador): 
     buscador.get("https://notaspersonales.free.nf/")

     
     password = buscador.find_element(By.NAME,"password") 
     password.send_keys(contras)

     time.sleep(10)

     login_button_incorrecto = WebDriverWait(buscador, 25).until(
        Ec.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
     )
     login_button_incorrecto.click()
     time.sleep(10)

    

