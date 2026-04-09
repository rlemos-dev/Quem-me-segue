from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from getpass import getpass

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

# Iniciar o Chrome com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.instagram.com')

time.sleep(10)

username= input('digite seu nome de usuário: ')
login = driver.find_element(By.XPATH, '//input[@name="username"]')
login.send_keys(username)

time.sleep(10)

senha= driver.find_element(By.XPATH, '//input[@name="password"]')
senha.send_keys(getpass('digite a senha do seu perfil: '))

time.sleep(10)

botao = driver.find_element(By.XPATH, '//button[@class=" _aswp _aswr _aswu _asw_ _asx2"]')
botao.click()

time.sleep(30)

driver.get(f'https://www.instagram.com/{username}')

time.sleep(15)

lista_seguidores= []
seguidores= driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
seguidores.click()

time.sleep(100)

barra= driver.find_element(By.XPATH, "//div[@role='dialog']//div[contains(@class,'x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6')]")

# Rola até o final
import time

last_count = 0
same_count_times = 0

while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', barra)
    time.sleep(2)

    users = barra.find_elements(By.XPATH, './/a[contains(@href, "/")]')
    current_count = len(users)

    # Se o número de usuários não aumenta por várias iterações, terminou
    if current_count == last_count:
        same_count_times += 1
        if same_count_times >= 3:  # tentou 3x e não mudou
            break
    else:
        same_count_times = 0  # resetar o contador se aumentou

    last_count = current_count

# Coletar nomes dos usuários
users = barra.find_elements(By.XPATH, './/a[contains(@href, "/")]')
for u in users:
    nome= u.text.strip()
    if nome and nome not in lista_seguidores:
        lista_seguidores.append(nome)

time.sleep(5)

driver.get(f'https://www.instagram.com/[{username}]')

time.sleep(15)

lista_seguindo= []
seguindo= driver.find_element(By.XPATH, '//a[contains(@href, "/following/")]')
seguindo.click()

time.sleep(100)

barra_seguindo= driver.find_element(By.XPATH, "//div[@role='dialog']//div[contains(@class,'x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6')]")

# Rola até o final
last_count = 0
same_count_times = 0

while True:
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', barra_seguindo)
    time.sleep(2)

    users = barra_seguindo.find_elements(By.XPATH, './/a[contains(@href, "/")]')
    current_count = len(users)

    # Se o número de usuários não aumenta por várias iterações, terminou
    if current_count == last_count:
        same_count_times += 1
        if same_count_times >= 3:  # tentou 3x e não mudou
            break
    else:
        same_count_times = 0  # resetar o contador se aumentou

    last_count = current_count

# Coletar nomes dos usuários
users = barra_seguindo.find_elements(By.XPATH, './/a[contains(@href, "/")]')
for u in users:
    nome= u.text.strip()
    lista_seguindo.append(nome)

driver.quit()

#####
nao_me_seguem= []

for pessoa in lista_seguindo:
    if pessoa not in lista_seguidores:
        nao_me_seguem.append(pessoa)
        

def salvar_lista(nome_arquivo, lista):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for item in lista:
            f.write(item + "\n")

salvar_lista("seguindo.txt", lista_seguindo)
salvar_lista("seguidores.txt", lista_seguidores)
salvar_lista("nao_me_seguem.txt", nao_me_seguem)

print(len(lista_seguindo))
print(len(lista_seguidores))
print(len(nao_me_seguem))