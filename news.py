import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

#Faz a requisição
response = requests.get('https://g1.globo.com/')

#Pega o conteudo da requisição
content = response.content

#Convertemos o conteudo para um objeto do beautfulSoup e nomeamos de site
site = BeautifulSoup(content, 'html.parser') #Convertendo Html para um objeto BeautifulSoup

# HTML da noticia - Vai dentro do site e encontra uma div cuja a classe é 'feed-post-body', ao encontrar a div jogamos na variavel noticia
noticias = site.find_all('div', attrs={'class': 'feed-post-body'}) #Retorna todas as noticias

for noticia in noticias:

 titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})

subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

if (subtitulo):
 lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
else: 
 lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo','Subtitulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)

print(news)