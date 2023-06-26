#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import minha_senha

link_licao = input('Insira o link da aula: ')

tipo_de_licao = input('''Digite 1 se essa lição deve ser inserido no deck de Escrita Japonesa
Digite 2 se essa lição deve ser inserido no deck de Frases em Japonês: ''')

site_lento = input('O site está lento? y/n ').casefold()

tempo_espera = 15 if site_lento =='y' else 5

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


# In[ ]:


#login no site da PJO
navegador.get(r'https://portal.programajaponesonline.com.br/login/')
time.sleep(tempo_espera)
navegador.find_element(By.ID, 'user_login').send_keys(minha_senha.login_jpo)
navegador.find_element(By.ID, 'user_pass').send_keys(minha_senha.senha_jpo)
navegador.find_element(By.ID, 'wp-submit').click()
time.sleep(tempo_espera)


# In[ ]:


#entra na lição
navegador.get(link_licao)
time.sleep(tempo_espera)

lista_botao = navegador.find_elements(By.CLASS_NAME, 'expand-card')
fronts = navegador.find_elements(By.CLASS_NAME, 'card-front')
backs = navegador.find_elements(By.CLASS_NAME, 'card-back')

#expandindo todas as caixas de texto
for botao in lista_botao:
    botao.click() 
    time.sleep(3)
    
#pega as frentes dos cards
lista_frentes = [frente.text for frente in fronts]   

#pega as traseiras dos cards
lista_tras = [tras.text for tras in backs]


# In[ ]:


#verificando as frentes e as traseiras do cards
print(lista_frentes)
print(lista_tras)

#caso haja algum item vazio, interrompe o código
for item in lista_frentes:
    if item == '':
        exit()
        time.sleep(5)


# In[ ]:


#verificando visualmente qual a quantidade de frases que serão adicionadas no Anki
print(len(lista_frentes))
print(len(lista_tras))


# In[ ]:


#login no ankiweb
navegador.get(r'https://ankiweb.net/account/login')
time.sleep(tempo_espera)
campos = navegador.find_elements(By.CLASS_NAME, 'form-control')
campos[0].send_keys(minha_senha.login_anki)
campos[1].send_keys(minha_senha.senha_anki)
navegador.find_element(By.XPATH, '/html/body/main/form/div[3]/button').click()
time.sleep(tempo_espera)
navegador.get(r'https://ankiuser.net/edit/')
time.sleep(tempo_espera)


# In[ ]:


if tipo_de_licao == '1':
    #opção Escrita Japonesa
    navegador.find_element(By.ID, 'deck').send_keys('Escrita em Japonês')

elif tipo_de_licao == '2':
    #opção Frases em Japonês
    navegador.find_element(By.ID, 'deck').send_keys('Frases em Japonês')

else:
    #deck de testes
    navegador.find_element(By.ID, 'deck').send_keys('testes')

time.sleep(3)


# In[ ]:


#criando o card
for i, botao in enumerate(lista_botao):
    navegador.find_element(By.ID, 'f0').send_keys(lista_frentes[i])
    navegador.find_element(By.ID, 'f1').send_keys(lista_tras[i])
    time.sleep(3)
    navegador.find_element(By.XPATH, '/html/body/main/p/button').click()
    time.sleep(3)


# In[ ]:


#fechando o navegador
navegador.close()

