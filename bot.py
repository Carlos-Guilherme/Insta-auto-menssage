import re
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os


class Menssager:
    def __init__(self, headless):
        service = Service(executable_path='geckodriver.exe')
        self.driver = webdriver.Firefox(service=service)
        
        if headless == True:
            options = Options()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=service, options=options)
        else:
            pass

    def entrar_na_conta(self, username, password):
        os.system('cls')
        print('Entrando no site...')
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        os.system('cls')
        print('Preenchendo formulário...')
        username_input = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.click()
        username_input.send_keys(username)
        time.sleep(2)
        
        password_input = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.click()
        password_input.send_keys(password)
        time.sleep(2)
        
        login_button = self.driver.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        os.system('cls')
        print('Finalizando Login...')
        time.sleep(15)
        
        try:
            # clicar em "agora não" se houver
            not_now_button = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            not_now_button.click()
        except NoSuchElementException:
            pass

    def enviar_texto(self, perfis, texto):
        self.nomes_perfis = re.findall(r"Foto do perfil de (.+)", perfis)
        self.contas_incentivadas = 0
        os.system('cls')
        for nome in self.nomes_perfis:
            
            try:
                print(f'Contas incentivadas: {self.contas_incentivadas}')
                self.driver.get(f"https://www.instagram.com/{nome}")
                time.sleep(5)
                try:
                    button_enviar_mensagem = self.driver.find_element('css selector', 'div.xjqpnuy')
                    button_enviar_mensagem.click()
                    
                    time.sleep(5)
                    try:
                        
                        button_agoranao = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                        button_agoranao.click()
                        campo_texto = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                        campo_texto.click()
                        for i in texto:
                            campo_texto.send_keys(i)
                        campo_texto.send_keys(Keys.ENTER)
                        self.contas_incentivadas += 1
                        time.sleep(2)
                    except NoSuchElementException:
                        campo_texto = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                        campo_texto.click()
                        for i in texto:
                            campo_texto.send_keys(i)
                        campo_texto.send_keys(Keys.ENTER)
                        self.contas_incentivadas += 1
                        time.sleep(2)
                except NoSuchElementException:
                    os.system('cls')
                    print(f'Contas incentivadas: {self.contas_incentivadas}')
                    self.driver.get("https://www.instagram.com/direct/inbox/")
                    time.sleep(5)

                    try:
                        button_agoranao = self.driver.find_element('css selector', 'button._a9--:nth-child(2)')
                        button_agoranao.click()
                        time.sleep(1)

                        button_enviar_mensagem = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')
                        button_enviar_mensagem.click()
                        

                        time.sleep(1)
                        entrada_pesquisar_user = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')
                        entrada_pesquisar_user.send_keys(nome)

                        time.sleep(3)
                        marcar_perfil = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/label/div/input')
                        marcar_perfil.click()

                        #checar se o primeiro perfil da lista corresponde ao perfil procurado
                        """primeiro_perfil = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div/span/span/span')
                        print(primeiro_perfil.text)"""

                        button_bp = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
                        button_bp.click()
                        time.sleep(3)
                        campo_texto = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                        campo_texto.click()
                        for i in texto:
                            campo_texto.send_keys(i)
                        campo_texto.send_keys(Keys.ENTER)
                        self.contas_incentivadas += 1
                        time.sleep(2)
                    except NoSuchElementException: 
                        time.sleep(1)
                        button_enviar_mensagem = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')
                        button_enviar_mensagem.click()
                        

                        time.sleep(1)
                        entrada_pesquisar_user = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')
                        entrada_pesquisar_user.send_keys(nome)

                        time.sleep(3)
                        marcar_perfil = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/label/div/input')
                        marcar_perfil.click()

                        #checar se o primeiro perfil da lista corresponde ao perfil procurado
                        """primeiro_perfil = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div/span/span/span')
                        print(primeiro_perfil.text)"""


                        button_bp = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
                        button_bp.click()
                        time.sleep(3)
                        campo_texto = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                        campo_texto.click()
                        for i in texto:
                            campo_texto.send_keys(i)
                        campo_texto.send_keys(Keys.ENTER)
                        self.contas_incentivadas += 1
                        time.sleep(2)
               
                try:
                    button_agoranao = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                    button_agoranao.click()
                    campo_texto = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                    campo_texto.click()
                    for i in texto:
                        campo_texto.send_keys(i)
                    campo_texto.send_keys(Keys.ENTER)
                    self.contas_incentivadas += 1
                    time.sleep(2)
                except NoSuchElementException:
                    pass
            except NoSuchElementException:
                os.system('cls')
                print(f'Contas incentivadas: {self.contas_incentivadas}')
                self.driver.get("https://www.instagram.com/direct/inbox/")
                time.sleep(5)

                button_agoranao = self.driver.find_element('css selector', 'button._a9--:nth-child(2)')
                button_agoranao.click()

                time.sleep(1)
                button_enviar_mensagem = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')
                button_enviar_mensagem.click()
                

                time.sleep(1)
                entrada_pesquisar_user = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')
                entrada_pesquisar_user.send_keys(nome)

                time.sleep(3)
                marcar_perfil = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/label/div/input')
                marcar_perfil.click()

                #checar se o primeiro perfil da lista corresponde ao perfil procurado
                primeiro_perfil = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div/span/span/span')
                print(primeiro_perfil.text)


                button_bp = self.driver.find_element('xpath', '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
                button_bp.click()
                time.sleep(3)

                campo_texto = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                campo_texto.click()

                for i in texto:
                    campo_texto.send_keys(i)
                campo_texto.send_keys(Keys.ENTER)
                self.contas_incentivadas += 1
                time.sleep(2)
               
                
    



