# controle de estoque

class Estoque:
    def __init__(self, arquivo:str) -> None:
        self._arquivo = arquivo

    def abrir_dados(self):
        arquivo = open(self._arquivo, 'r', encoding='UTF-8')
        conteudo = arquivo.read()

        lista = conteudo.split()

        arquivo.close()
        return lista

    def exibir_tabela_estoque(self):
        lista = self.abrir_dados()
        cabecalho = []
        estoque = dict()
        i = 0
        while i < 3:
            cabecalho.append(lista[i])
            i += 1

        for item in lista:
            if item is not cabecalho:
                if item.isdigit()




        return cabecalho