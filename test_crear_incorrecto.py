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

def test_login(buscador): 
     buscador.get("https://notaspersonales.free.nf/")

     email = WebDriverWait(buscador, 10).until(  
        Ec.presence_of_element_located((By.NAME,"username")) 
     )
     email.send_keys(usuario)

     password = buscador.find_element(By.NAME,"password") 
     password.send_keys(contras)

     login_button = WebDriverWait(buscador, 10).until(
        Ec.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
     )
     login_button.click()
  

def test_crear_nota(buscador):
   

    boton_crear = WebDriverWait(buscador, 10).until(
    Ec.element_to_be_clickable((By.LINK_TEXT, "Crear nueva nota"))
    )
    boton_crear.click()


    contenido = buscador.find_element(By.NAME, "contenido")
    contenido.send_keys("Contenido de prueba para la nota con selenium.")

    boton_guardar = buscador.find_element(By.XPATH, "//button[@type='submit']")
    boton_guardar.click()

    time.sleep(15)
