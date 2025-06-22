from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo

    @abstractmethod
    def encender(self):
        pass

    def apagar(self):
        print(f"{self.__class__.__name__} {self._modelo} apagado.")

class Computadora(Dispositivo):
    def __init__(self, marca, modelo, ram_gb):
        super().__init__(marca, modelo)
        self.ram_gb = ram_gb

    def encender(self):
        print(f"Computadora {self._marca} {self._modelo} con {self.ram_gb}GB RAM encendida.")

class Telefono(Dispositivo):
    def __init__(self, marca, modelo, camara_mp):
        super().__init__(marca, modelo)
        self.camara_mp = camara_mp

    def encender(self):
        print(f"Teléfono {self._marca} {self._modelo} con cámara de {self.camara_mp}MP encendido.")

class Tablet(Dispositivo):
    def __init__(self, marca, modelo, pulgadas):
        super().__init__(marca, modelo)
        self.pulgadas = pulgadas

    def encender(self):
        print(f"Tablet {self._marca} {self._modelo} de {self.pulgadas}\" encendida.")
