from bs4 import BeautifulSoup

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
        <li id='numero'>numérica</li>
        <li>ordenada</li>
    </ol>
</body>
</html>"""

html_parceado = BeautifulSoup(html,"html.parser")
# Imprimir saída html identado
print(html_parceado.prettify())

# Método find()

print(html_parceado.find('h2'))
print(html_parceado.find(class_ = 'first'))
print(html_parceado.find(id = 'numero'))

# Método find_all()
print(html_parceado.find_all('li'))