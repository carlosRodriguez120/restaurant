from cgitb import text
from tkinter import *
from turtle import left

# iniciar aplicacion

aplicacion = Tk()
aplicacion.geometry("1020x630")

# que no sea responsive
aplicacion.resizable(0, 0)

# titulo
aplicacion.title("HAMBURGUESAS CACERAS")

# COLOR DE FONDO
aplicacion.config(bg="LightCyan")

# panel superior
panelSuperior = Frame(aplicacion, bd=5, relief=SUNKEN)
panelSuperior.pack(side=TOP)

# etiqueta titulo
etiquetaTitulo = Label(panelSuperior, text="SISTEMA DE FACTURACION",
                       fg="Gray", font=("Dosis", 30), bg="Turquoise", width=42)
etiquetaTitulo.grid(row=0, column=0)
# panel izquierdo

panelIzquierdo = Frame(aplicacion, bd=2, relief=SUNKEN)
panelIzquierdo.pack(side=LEFT)

# panel costos
panelCostos = Frame(panelIzquierdo, bd=2, relief=SUNKEN)
panelCostos.pack(side=BOTTOM)

# panel comidas

panelComidas = LabelFrame(panelIzquierdo, text="Comidas", font=(
    "Dosis", 19, "bold"), bd=2, relief=SUNKEN, fg="Gray")
panelComidas.pack(side=LEFT)

# panel bebidas
panelComidas = LabelFrame(panelIzquierdo, text="Comidas ", font=(
    "Dosis", 19, "bold"), bd=2, relief=SUNKEN, fg="Gray")
panelComidas.pack(side=LEFT)


# evitar que la pantalla se cierre
aplicacion.mainloop()
