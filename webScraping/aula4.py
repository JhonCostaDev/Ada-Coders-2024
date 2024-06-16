from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            background-color: rgb(5, 72, 128);
            color: white;
        }

        .destaque {
            color: blue;
            font-weight: bolder;
        }
        #secondP {
            background-color: rgb(170, 182, 178);
            color: blue;
        }
    </style>
    <title>Document</title>
</head>
<body>
    <h1>Exemplos de Classes, IDs e Links</h1>

    <p>Aqui está um exemplo em <span class="destaque">destaque</span>.</p>

    <p id="secondP">Este é um parágrafo com ID, seu fundo é cinza claro.</p>

    <p>Visite <a href="exemplo.com">este</a> exemplo para mais informações.</p>
    
</body>
</html>"""

html_parsed = BeautifulSoup(html,"html.parser")

# Encontrar Texto em destaque

texto_destaque = html_parsed.find(class_ ='destaque')
print(texto_destaque)

link = html_parsed.find('a')
print(link)