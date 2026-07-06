# Nombre: TU NOMBRE
# Grupo: 213023_30
from abc import ABC, abstractmethod
from validaciones import ClienteInvalido
from logs import registrar_log

class Entidad(ABC):
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    @abstractmethod
    def mostrar(self):
        pass

class Cliente(Entidad):
    def __init__(self, id, nombre, email):
        super().__init__(id)
        self.__nombre = nombre
        self.__email = email
        self.validar()

    def validar(self):
        if not self.__nombre or len(self.__nombre) < 3:
            registrar_log(f"Error: Nombre de cliente invalido")
            raise ClienteInvalido("El nombre debe tener minimo 3 letras")
        if "@" not in self.__email:
            registrar_log(f"Error: Email invalido {self.__email}")
            raise ClienteInvalido("Email debe contener @")

    def mostrar(self):
        return f"Cliente: {self.get_id()} | {self.__nombre} | {self.__email}"

class Servicio(Entidad):
    def __init__(self, id, nombre, precio_base):
        super().__init__(id)
        self.nombre = nombre
        self.__precio_base = precio_base

    def get_precio_base(self):
        return self.__precio_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass

    def mostrar(self):
        return f"Servicio: {self.nombre}"