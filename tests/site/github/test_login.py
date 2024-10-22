from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class TestLogin:
    def setup_class(self):
        global driver  ## Deixa a variável global para outros métodos
        # Define o navegador que será usado
        driver = webdriver.Chrome()
        # Deixar em tela fullscreen para evitar problemas com responsividade
        driver.maximize_window()
    
    def test_login(self):
        # Define qual página o browser deve abrir
        driver.get('https://github.com/')

        # Procuramos pelo link de login
        btn_link_sign_in = driver.find_element(By.CLASS_NAME, 'HeaderMenu-link--sign-in')
        # Simulamos o clique no link
        btn_link_sign_in.click()

        # Realizamos uma captura de tela
        driver.save_screenshot('Screen_00.png')

        # Aguarda dois segundos
        time.sleep(2)

        field_login = driver.find_element(By.ID, 'login_field')
        field_login.send_keys('email@satellasoft.com')

        field_password = driver.find_element(By.ID, 'password')
        field_password.send_keys('adminadmin')

        # Realizamos uma captura de tela
        driver.save_screenshot('Screen_01.png')

        field_password.send_keys(Keys.RETURN)
        # Aguarda dois segundos
        time.sleep(2)

        label_result = driver.find_element(By.CLASS_NAME, 'js-flash-alert')

        # Realizamos uma captura de tela
        driver.save_screenshot('Screen_02.png')
        print(label_result.text)

        assert 'Incorrect username or password.' in label_result.text
        # assert 'meu email está errado' in label_result.text

    def teardown_class(self):
        driver.close