class Teste:
    def __init__(self):
        self.x = 5

    def up(self):
        self.x += 1
    def down(self):
        self.x -= 1

    def subir(self):
        if self.x > 0:
            self.up()

    def __str__(self):
        return f'{self.x}'

t1 = Teste()
print(t1)
t1.subir()
t1.subir()
t1.subir()
print(t1)
