# Site utilizado no exemplo
# https://www.scrapethissite.com/pages/simple/
# Programa que exibir países e suas capitais

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