import tkinter as tk
from datetime import date

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora de Edad")
        self.ventana1.geometry('400x200')

        # Etiqueta de instrucción
        self.label1 = tk.Label(self.ventana1, text="Ingrese su año de nacimiento:")
        self.label1.grid(column=0, row=0, padx=10, pady=10)

        # Entrada de año
        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=10, pady=10)

        # Botón para calcular
        self.boton1 = tk.Button(self.ventana1, text="Calcular Edad", command=self.calcular)
        self.boton1.grid(column=0, row=1, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado
        self.label2 = tk.Label(self.ventana1, text="Tu edad aparecerá aquí")
        self.label2.grid(column=0, row=2, columnspan=2, pady=10)

        self.ventana1.mainloop()

    def calcular(self):
        try:
            anio_nacimiento = int(self.dato1.get())
            anio_actual = date.today().year
            edad = anio_actual - anio_nacimiento

            if edad < 0:
                self.label2.configure(text="Error: Año no válido")
            else:
                self.label2.configure(text=f"Tienes {edad} años")
        except ValueError:
            self.label2.configure(text="Por favor ingrese un número válido")

# Ejecutar la app
aplicacion1 = Aplicacion()
