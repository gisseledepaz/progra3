import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora de Promedio")
        self.ventana1.geometry('1000x180')

        # Lab1
        self.label1 = tk.Label(self.ventana1, text="Ingrese nota de Lab1 (30%):")
        self.label1.grid(column=0, row=0, padx=10, pady=5, sticky="w")
        self.lab1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.lab1)
        self.entry1.grid(column=1, row=0, padx=10, pady=5)

        # Lab2
        self.label2 = tk.Label(self.ventana1, text="Ingrese nota de Lab2 (30%):")
        self.label2.grid(column=0, row=1, padx=10, pady=5, sticky="w")
        self.lab2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana1, width=10, textvariable=self.lab2)
        self.entry2.grid(column=1, row=1, padx=10, pady=5)

        # Parcial
        self.label3 = tk.Label(self.ventana1, text="Ingrese nota del Parcial (40%):")
        self.label3.grid(column=0, row=2, padx=10, pady=5, sticky="w")
        self.parcial = tk.StringVar()
        self.entry3 = tk.Entry(self.ventana1, width=10, textvariable=self.parcial)
        self.entry3.grid(column=1, row=2, padx=10, pady=5)

        # Botón para calcular
        self.boton1 = tk.Button(self.ventana1, text="Calcular Promedio", command=self.calcular)
        self.boton1.grid(column=0, row=3, columnspan=2, pady=15)

        # Resultado
        self.resultado = tk.Label(self.ventana1, text="Su promedio aparecerá aquí")
        self.resultado.grid(column=0, row=4, columnspan=2, pady=10)

        self.ventana1.mainloop()

    def calcular(self):
        try:
            nota1 = float(self.lab1.get())
            nota2 = float(self.lab2.get())
            nota3 = float(self.parcial.get())

            # Calcular promedio ponderado
            promedio = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)

            self.resultado.configure(text=f"Su promedio es: {promedio:.2f}")
        except ValueError:
            self.resultado.configure(text="Por favor ingrese solo números válidos")


# Ejecutar la app
aplicacion1 = Aplicacion()


