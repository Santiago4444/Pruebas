from tkinter import *
import re

from Resultados_Pantalla import *


def pulsaciones_teclas(self, valor, mostrar):
    if mostrar == True:  # Si es un nro
        self.operacion += str(valor)
        # self.mostrar_pantalla(valor)
        mostrar_pantalla(self, valor)
    elif not mostrar and valor == "=":
        self.operacion = re.sub(u"\u00d7", "*", self.operacion)
        borrar_pantalla(self)
        mostrar_pantalla(self,
                         str(eval(self.operacion)))  # ver funcion EVAL
    else:
        pass
