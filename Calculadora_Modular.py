from tkinter import *
# Linea de separacion antes de nuestros modulos:
from Botonera_Calculadora import *

raiz = Tk()


class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora POO")

        self.operacion = ""

        # Display:
        self.display = Entry(ventana, font="Arial 15")
        self.display.grid(row=1, column=0, columnspan=4, pady=10)
        self.display.config(bg="black", fg="#00db00",
                            justify="right", width=25)

        # Creacion de botones:
        # le enviamos como parametro el Objeto Calculadora al metodo del otro modulo:
        boton7 = colocar_Boton(self, 7)
        boton8 = colocar_Boton(self, 8)
        boton9 = colocar_Boton(self, 9)
        botondiv = colocar_Boton(self, "/")

        boton4 = colocar_Boton(self, 4)
        boton5 = colocar_Boton(self, 5)
        boton6 = colocar_Boton(self, 6)
        botonx = colocar_Boton(self, u"\u00d7")

        boton1 = colocar_Boton(self, 1)
        boton2 = colocar_Boton(self, 2)
        boton3 = colocar_Boton(self, 3)
        botonrest = colocar_Boton(self, "-")

        botoncero = colocar_Boton(self, 0)
        botoncoma = colocar_Boton(self, ".")
        botonigual = colocar_Boton(self, "=", mostrar=False)
        botonmas = colocar_Boton(self, "+")

        botones = [boton7, boton8, boton9, botondiv, boton4, boton5, boton6, botonx,
                   boton1, boton2, boton3, botonrest, botoncero, botoncoma, botonigual, botonmas]
        construir_botones(self, botones, 4)  # 4 filas de botones


mi_calculadora = Calculadora(raiz)

raiz.mainloop()
