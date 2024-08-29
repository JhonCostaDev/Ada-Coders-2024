class Esfera:
    def __init__(self, raio:float) -> None:
        self.raio = raio
        self.pi = 3.1415
        
    def volume(self) -> float:
        volume_calculado = (4/3) * self.pi * (self.raio ** 3)
        return volume_calculado
    
    def area_superficie(self) -> float:
        area_calculada = 4 * self.pi * (self.raio ** 2)
        return area_calculada
    