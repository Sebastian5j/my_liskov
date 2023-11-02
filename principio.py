
from abc import ABCMeta, abstractmethod

class Transporte(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, **kwargs):
        self._pasajeros = kwargs["pasajeros"]

    def transportar(self):
        pass

class Auto(Transporte):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    def transportar(self):
        print(f"Soy el auto y transporto {self._pasajeros} pasajeros") 
 
class Moto(Transporte):
    def transportar(self):
        print(f"Soy la moto y transporto {self._pasajeros} pasajeros")


class Avion(Transporte):
    def transportar(self):
        print(f"Soy el avión y transporto {self._pasajeros} pasajeros")

class Chofer():
    def manejar(self,transporte: Transporte):
        print("Soy el chofer y voy a arrancar el transporte")
        transporte.transportar()

if __name__ == "__main__":
    auto_chevy = Auto(pasajeros = 4)
    #auto_chevy.transportar()

    auto_winstar = Auto(pasajeros = 8)
    #auto_winstar.transportar()
    
    mis_transportes = [auto_chevy, auto_winstar]
    chofer = Chofer()
    for transporte in mis_transportes:
        chofer.manejar(transporte)
