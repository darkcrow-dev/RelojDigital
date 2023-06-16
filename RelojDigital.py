from tkinter import *
from time import strftime

#reloj digital
def actualizarReloj():
    hora_minutos.config(text = strftime("%H:%M"))
    segundos.config(text = strftime("%S"))
    fecha.config(text = strftime("%A, %d/%m/%Y"))
    segundos.after(1000, actualizarReloj)
    return

ventana = Tk()
ventana.title("Reloj digital")

ventanaHoraFecha = Frame()
ventanaHoraFecha.pack()

hora_minutos = Label(ventanaHoraFecha, font = ("Arial", 100), text = "H:M")
hora_minutos.grid(row = 0, column = 0)

segundos = Label(ventanaHoraFecha, font = ("Arial", 50), text = "s")
segundos.grid(row = 0, column = 1, sticky = "n")

fecha = Label(font = ("Arial", 50), text = "dia d/m/aaaa")
fecha.pack(anchor = "center")

actualizarReloj()

ventana.mainloop()