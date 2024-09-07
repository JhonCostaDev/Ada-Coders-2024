import time
# Decoradores
def calcular_tempo(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time() - start
        print(f'Tempo decorrid0 {func.__name__}:{end}')
    return wrapper

@calcular_tempo
def goiava():
    for i in range(0, 10):
        print(f'Número = {i}')
        time.sleep(0.5)
        
goiava()