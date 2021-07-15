from tkinter import *

from Operaciones_Calculadora import *

# contador = 0


def construir_botones(self, botones, filas_botones):
    # self hace referencia a la calculadora modular
    # boton hace referencia a los botones individuales que vayamos construyendo
    # filas_botones es para poder indicarle cuantas filas de botones queremos
    contador = 0
    # Rellenar el grid de la calculadora despues del display:
    for fila in range(2, filas_botones+2):
        for columna in range(4):
            botones[contador].grid(row=fila, column=columna)
            contador += 1


def colocar_Boton(self, valor, mostrar=True, ancho=9, alto=1):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 9),
                  command=lambda: pulsaciones_teclas(self, valor, mostrar))
