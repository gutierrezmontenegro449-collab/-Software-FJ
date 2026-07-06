# Nombre: Miguel angel baron gutierrez
# Grupo: 213023_30

from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.__nombre = nombre
        self.__precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    def describir(self):
        return f"Servicio: {self.__nombre}"

    def get_precio_base(self):
        return self.__precio_base

class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion):
        return self.get_precio_base() * duracion * 1.19

    def describir(self):
        return "Alquiler de equipo tecnológico"

class ReservaPersonalizada(Servicio):
    def calcular_costo(self, duracion):
        return 20000 + (self.get_precio_base() * duracion)

    def describir(self):
        return "Reserva con servicios adicionales"

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion):
        self.id = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.__estado = "Pendiente"

    def mostrar(self):
        costo = self.servicio.calcular_costo(self.duracion)
        return f"Reserva {self.id} | Estado: {self.__estado} | Costo: {costo}"