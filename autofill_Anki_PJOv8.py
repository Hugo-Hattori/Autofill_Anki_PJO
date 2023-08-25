#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import infos
from tkinter import *
from tkinter import messagebox


link_licao = input('Insira o link da aula: ')

tipo_de_licao = input('''Digite 1 se essa lição deve ser inserido no deck de Escrita Japonesa
Digite 2 se essa lição deve ser inserido no deck de Frases em Japonês: ''')

servico = Service()
opcoes = Options()
opcoes.add_argument("--start-maximized")
navegador = webdriver.Chrome(service=servico, options=opcoes)


# In[8]:


def esperar_carregar(elemento):
    while len(navegador.find_elements(By.CLASS_NAME, elemento)) < 1:
        time.sleep(1)
    time.sleep(2)


# In[9]:


#login no site da PJO
navegador.get(r'https://portal.programajaponesonline.com.br/login/')
esperar_carregar('input')
navegador.find_element(By.ID, 'user_login').send_keys(infos.login_jpo)
navegador.find_element(By.ID, 'user_pass').send_keys(infos.senha_jpo)
navegador.find_element(By.ID, 'wp-submit').click()
esperar_carregar('menu-item')


# In[10]:


#entra na lição
navegador.get(link_licao)
esperar_carregar('single-box-content')

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


# In[11]:


#verificando as frentes e as traseiras do cards
print(lista_frentes)
print(lista_tras)

#caso haja algum item vazio, interrompe o código
for item in lista_frentes:
    if item == '':
        navegador.close()


# In[12]:


#verificando visualmente qual a quantidade de frases que serão adicionadas no Anki
print(len(lista_frentes))
print(len(lista_tras))


# In[13]:


#login no ankiweb
navegador.get(r'https://ankiweb.net/account/login')
esperar_carregar('form-control')
campos = navegador.find_elements(By.CLASS_NAME, 'form-control')
campos[0].send_keys(infos.login_anki)
campos[1].send_keys(infos.senha_anki)
navegador.find_element(By.XPATH, '/html/body/div/main/form/div[3]/button').click()
esperar_carregar('btn-outline-secondary')
navegador.get(r'https://ankiuser.net/edit/')
esperar_carregar('form-group')


# In[14]:


if tipo_de_licao == '1':
    #opção Escrita Japonesa
    navegador.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/input').send_keys(infos.decks[0], Keys.TAB)

elif tipo_de_licao == '2':
    #opção Frases em Japonês
    navegador.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/input').send_keys(infos.decks[1], Keys.TAB)

else:
    #deck de testes
    navegador.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/input').send_keys(infos.decks[2], Keys.TAB)

time.sleep(3)


# In[15]:


#criando o card
for i, botao in enumerate(lista_botao):
    try:
        campos = navegador.find_elements(By.CLASS_NAME, 'form-control')
        campos[0].send_keys(lista_frentes[i])
        campos[1].send_keys(lista_tras[i])
        time.sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div/main/form/button').click()
        time.sleep(3)
    except:
        navegador.find_element(By.XPATH, '/html/body/main/form/button').send_keys(Keys.END)
        time.sleep(3)
        navegador.find_element(By.XPATH, '/html/body/div/main/form/button').click()
        time.sleep(3)


# In[16]:


#fechando o navegador
navegador.close()
janela = Tk()
messagebox.showinfo('Programa concluído com sucesso. Os seus cards foram criados!.')
janela.destroy()

