# Nombre: TU NOMBRE
# Grupo: 213023_30
from entidades import Servicio
from validaciones import ReservaFallida

class ReservaSala(Servicio):
    def calcular_costo(self, duracion, descuento=0):
        costo = self.get_precio_base() * duracion
        return costo - (costo * descuento)

    def describir(self):
        return "Alquiler de sala por horas"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion):
        return self.get_precio_base() * duracion * 1.19

    def describir(self):
        return "Alquiler de equipos tecnologicos"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion):
        return self.get_precio_base() + (duracion * 50000)

    def describir(self):
        return "Asesoria con experto"

class Reserva:
    def __init__(self, id, cliente, servicio, duracion):
        self.id = id
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.__estado = "Pendiente"

    def confirmar(self):
        try:
            if self.duracion <= 0:
                raise ReservaFallida("Duracion debe ser mayor a 0")
            self.__estado = "Confirmada"
            return "Reserva confirmada"
        except Exception as e:
            from logs import registrar_log
            registrar_log(f"Reserva fallida: {e}")
            raise
        finally:
            print("Proceso de confirmacion finalizado")

        def mostrar(self):
    costo = self.servicio.calcular_costo(self.duracion)
    return f"Reserva {self.id} | Estado: {self.__estado} | Costo: {costo}"