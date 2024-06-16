# WEB SCRAPING

## O que é?
Tradução literal: Raspagem da web, extração de dados

## Composição de uma página Web

1. HTML
2. CSS
3. JAVASCRIPT

* HTML: HYPER TEXT MARKUP LANGUAGE
É a base de toda página Web, Define todo o conteúdo e localização dos itens no navegador.

* CSS: Cascading Style Sheets
Defina os estilos, cores, tamanhos e formatos das páginas web.

## Biblioteca BeautifulSoup

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

Installing Beautiful Soup
If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

```bash
$ apt-get install python-bs4 (for Python 2)

$ apt-get install python3-bs4 (for Python 3)

```

### Exemplo de Uso
```python
from bs4 import BeautifulSoup

# atribuindo um documento html a uma variável
html = """<!DOCTYPE html> 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: black;
            color: white;
        }
    </style>
    <title>Página de Teste</title>
</head>
<body>
    <h1>Isso é um título</h1>
    <h2>Título de nível 2</h2>

    <p>Isso é um parágrafo</p>

    <ul>
        <li class = "first">lista</li>
        <li>não</li>
        <li>ordenada</li>
    </ul>

    <ol>
        <li>Lista</li>
        <li>numérica</li>
        <li>ordenada</li>
    </ol>
</body>
</html>"""

# Método parser, 
html_parceado = BeautifulSoup(html,"html.parser")

# Imprimir saída html identado
print(html_parceado.prettify())
```
## Principais Métodos

* Find(): Retorna o primeiro objeto procurado.

* Find_all(): Retorna uma lista de todos os objetos procurados.

```python
html_parceado = BeautifulSoup(html,"html.parser")
# Imprimir saída html identado
print(html_parceado.prettify())

# Método find()

print(html_parceado.find('h2'))
print(html_parceado.find(class_ = 'first'))
print(html_parceado.find(id = 'numero'))

# Método find_all()
print(html_parceado.find_all('li'))
```

## Como utilizar BeautifulSoup em sites reais.

```python
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.scrapethissite.com/pages/simple/').text
html_parsed = BeautifulSoup(html,"html.parser")

#print(html_parsed.prettify())

# Pegando o nome do país
# .text retira as tags html, retornando apenas o texto com espaços
# .strip() elimina os espaços desnecessários
country_name = html_parsed.find(class_ = 'country-name').text.strip()

country_capital = html_parsed.find(class_ = 'country-capital').text.strip()
#print(f'País: {country_name} e Capital: {country_capital}')

# atribuindo os países a uma lista
country_list = html_parsed.find_all(class_ = 'country-name')
capitals_list = html_parsed.find_all(class_ = 'country-capital')

country_e_capital = []

for country, capital in zip(country_list, capitals_list):
    dicionario = {
        "Pais" : country.text.strip(),
        "Capital" : capital.text.strip()
    }
    country_e_capital.append(dicionario)


print(country_e_capital)
```

## Como utilizar Selenium

Bibliotaca python voltada em simular interações de usuários em páginas web.

Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.

Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. The current supported Python versions are 3.5 and above.

### Quando utilizar?

* Interagir
* Localizar
* Extrair

# COMO LOCALIZAR E INTERAGIR COM O SELENIUM
```
//*[@id="username"]
<video is="castable-video" part="video" crossorigin="" playsinline="" cast-src="https://stream.mux.com/Vy5bURipuGCGHAjPODxF3unIt01cEGpKPTiqjgz00BEMQ.m3u8?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImF3Rk8ycUpMZnllRHBoS1Q2Um9DcTVVVTE1VDJwNmNxekpoYkNDWjdnMDJ3In0.eyJleHAiOjE3MTg2NjIwNDUsImF1ZCI6InYiLCJzdWIiOiJWeTViVVJpcHVHQ0dIQWpQT0R4RjN1bkl0MDFjRUdwS1BUaXFqZ3owMEJFTVEifQ.LF-pvHkWgBFMhUSqLcrMcZ7ki1AqXaH_p2_p4z0JD8A-fm7muMPl4XwKEUn-UPVIa-sPS1GR6S0UbiQomneqWIr1z7auEttukfD0Uh7DDRKUE0xS-bIyR1HvTiL1BwMenWW3fksg52KsaR7JgOwcvAQYzXW4wTFxUleIa2tU5ANmXZ-KjFbnIcG19kFYQg4f3CO6sr70cJCDkRlp-EhFYvMCQ4Ajwrlg0my6_6_B0hmR7JLi_rt7LuX-jk0V-PfmdlTxDLi3pBcoTwc10VRp0Fi_f4_4Vd3bO974e9-EEhliABvSiZmKAUwT0_hF950TPjYZEtVaxeJ2PB17BJqUZA" preload="metadata"><track label="thumbnails" default="" kind="metadata" src="https://image.mux.com/Vy5bURipuGCGHAjPODxF3unIt01cEGpKPTiqjgz00BEMQ/storyboard.vtt?format=webp"><source type="video/mp4" src="blob:https://comunidade.ada.tech/e7aca8dc-81d7-4cde-937c-8e3e00a5161c"><track kind="metadata" label="cuepoints" data-removeondestroy=""></video>
```