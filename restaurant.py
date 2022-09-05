from tkinter import *

# iniciar aplicacion

aplicacion = Tk()
aplicacion.geometry("1020x630")

# que no sea responsive
aplicacion.resizable(0, 0)

# titulo
aplicacion.title("HAMBURGUESAS CACERAS")

# COLOR DE FONDO
aplicacion.config(bg="burlywood")

# panel superior
panelSuperior = Frame(aplicacion, bd=2, relief=FLAT)
panelSuperior.pack(side=TOP)

# etiqueta titulo
etiquetaTitulo = Label(panelSuperior, text="SISTEMA DE FACTURACION",
                       fg="azure4", font=("dosis", 40), bg="burlywood", width=27)
etiquetaTitulo.grid(row=0,column=0)
# evitar que la pantalla se cierre
aplicacion.mainloop()
