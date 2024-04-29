import requests 
from bs4 import BeautifulSoup

link = "https://pt.wikipedia.org/wiki/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

pergunte = input('Sobre qual assunto falaremos hoje? \n')

link = f'https://pt.wikipedia.org/wiki/{pergunte}'

requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")

p = site.find_all('p')

for x in p:
    # Retirando <p></p>  sem nada
    if len(x.get_text()) > 10:
        print(f'\n{x.get_text()}')
    # Adicionando o próximo <p></p> se o atual for pequeno demais (complemento)
    if len(x.get_text()) > 500:
        break