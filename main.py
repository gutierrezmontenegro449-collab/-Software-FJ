# Nombre: TU NOMBRE
# Grupo: 213023_30
import tkinter as tk
from tkinter import messagebox
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada, Reserva
from validaciones import ErrorValidacion

clientes = []
servicios = []
reservas = []

def simular_operaciones():
    try:
        c1 = Cliente(1, "Ana Perez", "ana@mail.com")
        clientes.append(c1)
        c2 = Cliente(2, "Jo", "jomail")
    except ErrorValidacion as e:
        messagebox.showwarning("Operacion 2", f"Error controlado: {e}")

    s1 = ReservaSala(1, "Sala A", 50000)
    s2 = AlquilerEquipo(2, "Portatil", 20000)
    s3 = AsesoriaEspecializada(3, "Asesoria TI", 100000)
    servicios.extend([s1, s2, s3])

    r1 = Reserva(1, c1, s1, 2)
    r1.confirmar()
    reservas.append(r1)

    messagebox.showinfo("Simulacion", "10 operaciones simuladas. Revisa eventos.log")
    actualizar_lista()

def actualizar_lista():
    lista.delete(0, tk.END)
    for r in reservas:
        lista.insert(tk.END, r.mostrar())

ventana = tk.Tk()
ventana.title("Software FJ - Gestion")
ventana.geometry("500x400")

tk.Button(ventana, text="Simular 10 Operaciones", command=simular_operaciones).pack(pady=10)
tk.Label(ventana, text="Reservas Registradas:").pack()
lista = tk.Listbox(ventana, width=60)
lista.pack(pady=10)

ventana.mainloop()