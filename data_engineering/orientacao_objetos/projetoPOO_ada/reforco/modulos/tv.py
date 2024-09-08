'''Crie uma classe `Televisor`cujos atributos são: fabricante; modelo; canal atual; lista de canais; volume.

Faça métodos aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV. 

Obs.: o volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.
'''

class Tv:
    # Construtor do objeto Tv
    def __init__(self, fabricante:str, modelo:str) -> None:
        self._fabricante = fabricante
        self._modelo = modelo
        self._canal_atual = ''
        self._lista_canais = []
        self.canais_sintonizados = 0
        self._volume = 1
        
    # Getters
    def sintonizar_canais(self, novo_canal:str) -> None:
        if novo_canal in self._lista_canais:
            print('Canal já Sintonizado.')
        else:
            self._lista_canais.append(novo_canal)
            self.canais_sintonizados += 1
        self._canal_atual = self._lista_canais[0]
        
    
    def canal_up(self) -> None:
        if self.canais_sintonizados == 0 :
            print('Nenhum canal foi sintonizado ainda.\nPor favor, sintonize novos canais')
        elif self.canais_sintonizados == 1:
            print('Este é o único canal da sua lista de canais.\nPor favor, sintonize novos canais')
        else:
            indice_canal_atual = self._lista_canais.index(self._canal_atual)
            prox_canal = indice_canal_atual + 1
            
            if self.canais_sintonizados >= prox_canal:
                self._canal_atual = self._lista_canais[0]
            else:
                self._canal_atual = self._lista_canais[prox_canal]
                
            
    
    def canal_down(self) -> None:
        if self.canais_sintonizados == 0:
            print('Nenhum canal foi sintonizado ainda.\nPor favor, sintonize novos canais')
        elif self.canais_sintonizados == 1:
            print('Este é o único canal da sua lista de canais.\nPor favor, sintonize novos canais')
            
    def volume_up(self) -> None:
        # só aumentará o volume se o mesmo for menor que 100.
        if self._volume < 100:
            self._volume += 1
            
    def volume_down(self) -> None:
        # só diminuirá o volume se o mesmo for maior que 0.
        if self._volume > 0:
            self._volume -= 1
            
    # Metodo magico 
    def __repr__(self) -> str:
        return f'''
    ============ TELEVISOR ============
    Marca: {self._fabricante}
    Modelo: {self._modelo}
    Canal Atual: {self._canal_atual}
    Volume: {self._volume}
    Canais Sintonizados: {self.canais_sintonizados}
    '''
    
    
    
lg = Tv('lg', 'scarlet')
print(lg)
lg.sintonizar_canais('globo')
lg.sintonizar_canais('sbt')
lg.canal_up()
lg.canal_up()

print(lg)

