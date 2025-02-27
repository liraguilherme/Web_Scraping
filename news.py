import requests
from bs4 import BeautifulSoup

#Faz a requisição
response = requests.get('https://g1.globo.com/')

#Pega o conteudo da requisição
content = response.content

#Convertemos o conteudo para um objeto do beautfulSoup e nomeamos de site
site = BeautifulSoup(content, 'html.parser') #Convertendo Html para um objeto BeautifulSoup

# HTML da noticia - Vai dentro do site e encontra uma div cuja a classe é 'feed-post-body', ao encontrar a div jogamos na variavel noticia
noticia = site.find('div', attrs={'class': 'feed-post-body'}) #Retorna a noticia especifica dentro do inspecionar


#Titulo - Ao encontrar a noticia pedimos que vá até ela e encontre uma tag 'a' que tenha a classe 'feed-post-link' e jogamos na variavel titulo, assim obtendo o titulo da noticia
titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})

print(titulo)

#Pegar conteudo da noticia:
print(titulo.text)

#pegar subtitulo da noticia: 
#subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
#print(subtitulo.text)