# Funções Utilizadas em Main.py

def acesso_url(driver, username= None):
    try:
        if username:
            url= (f'https://www.instagram.com/{username}')
        else:
            url= (f'https://www.instagram.com')
    
        driver.get(url)

    except Exception as info:
        print(f'Erro ao acessar {url}: {info}')
