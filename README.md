# 📊 Quem-me-segue

Script em Python que automatiza o processo de análise do Instagram para identificar quais usuários você segue, mas que não te seguem de volta.

---

## 🚀 Sobre o projeto

Este projeto utiliza Selenium para simular ações no navegador, acessar sua conta do Instagram e coletar dados de:

- Seguidores
- Contas que você segue

Com base nesses dados, o script identifica automaticamente quem **não te segue de volta**.

---

## 🔗 Repositório

https://github.com/rlemos-dev/Quem-me-segue.git

---

## 🛠️ Tecnologias utilizadas

- Python  
- Selenium  
- ChromeDriver  

---

## ⚙️ Funcionalidades

- Login automatizado no Instagram  
- Coleta completa de seguidores  
- Coleta completa de contas seguidas  
- Comparação automática entre listas  
- Geração de arquivos com resultados  
- Exibição de métricas no terminal  

---

## 📦 Instalação

Clone o repositório:

git clone https://github.com/rlemos-dev/Quem-me-segue.git  
cd Quem-me-segue  

Instale as dependências:

pip install selenium  

Baixe o ChromeDriver compatível com sua versão do Google Chrome:  
https://chromedriver.chromium.org/downloads  

---

## ▶️ Como usar

Execute o script:

python main.py  

Depois:

1. Digite seu usuário do Instagram  
2. Digite sua senha (oculta por segurança)  
3. Aguarde o carregamento das listas  

---

## 📁 Saída

O script gera os seguintes arquivos:

- seguidores.txt → lista de seguidores  
- seguindo.txt → lista de contas seguidas  
- nao_me_seguem.txt → usuários que não te seguem de volta  

Também exibe no terminal:

- Total de seguidores  
- Total de seguindo  
- Total de não seguidores  

---

## ⚠️ Avisos importantes

- Este projeto utiliza automação de navegador (Selenium)  
- O Instagram pode limitar ou bloquear ações automatizadas  
- A estrutura do site pode mudar, exigindo atualização do código  
- Use com responsabilidade  

---

## 🧠 Como funciona

1. O script abre o navegador  
2. Realiza login no Instagram  
3. Acessa seu perfil  
4. Coleta a lista de seguidores  
5. Coleta a lista de contas seguidas  
6. Compara as listas  
7. Salva os resultados em arquivos  

---

## 📌 Melhorias futuras

- Interface gráfica (GUI)  
- Exportação para CSV/Excel  
- Uso de WebDriverWait no lugar de time.sleep  
- Otimização de performance  
- Filtros personalizados  

---

## 🤝 Contribuição

Contribuições são bem-vindas.  
Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📄 Licença

Projeto desenvolvido para fins educacionais.
