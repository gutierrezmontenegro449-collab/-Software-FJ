# Nombre: TU NOMBRE
# Grupo: 213023_30

class ErrorValidacion(Exception): pass
class ClienteInvalido(ErrorValidacion): pass
class ServicioNoDisponible(ErrorValidacion): pass
class ReservaFallida(ErrorValidacion): pass