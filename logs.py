# Nombre: TU NOMBRE
# Grupo: 213023_30
import datetime

def registrar_log(mensaje):
    try:
        with open("eventos.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now()} - {mensaje}\n")
    except Exception as e:
        print(f"No se pudo escribir en el log: {e}")
    else:
        pass
    finally:
        pass