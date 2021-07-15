from tkinter import *

raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

operacion = ""  # Variable que guarde el tipo de operacion elegida
resultado = 0

digitoDisplay = StringVar()  # Nro que se muestra en display, 1 caracter
display = Entry(miFrame, textvariable=digitoDisplay, font="Arial 15")

display.grid(row=1, column=1, columnspan=4, pady=10)
display.config(bg="black", fg="#00db00", justify="right", width=15)

digitoDisplay.set("0")

# ----------Pulsar coma ------------


def pulsacion_coma():
    contador_coma = 0
    for i in digitoDisplay.get():
        if i == ".":
            contador_coma += 1
    if contador_coma == 0:
        digitoDisplay.set(digitoDisplay.get()+".")

# ----------Pulsaciones Teclas (excepto la coma) ------


def pulsacionesTeclas(numeroPulsado):

    global operacion
    global coma
    if operacion != "":

        digitoDisplay.set(numeroPulsado)
        operacion = ""
    else:
        # Si pulso un cero y hay un cero en el display:
        if numeroPulsado == "0" and digitoDisplay.get() == "0":
            digitoDisplay.set("0")
        # Si pulso . y hay un cero:
        elif numeroPulsado == "." and digitoDisplay.get() == "0":
            digitoDisplay.set(digitoDisplay.get()+numeroPulsado)

        # Si pulso otro nro que no sea cero y hay cero en el display:
        elif numeroPulsado != "0" and digitoDisplay.get() == "0":
            digitoDisplay.set(numeroPulsado)

        elif numeroPulsado == "." and coma == False:
            digitoDisplay.set(digitoDisplay.get()+numeroPulsado)

        elif numeroPulsado != ".":
            digitoDisplay.set(digitoDisplay.get()+numeroPulsado)


# ----------Funcion Suma-------------


def suma(num):
    global operacion
    global resultado
    resultado += float(num)
    if resultado.is_integer():
        digitoDisplay.set(int(resultado))
        operacion = "suma"
    else:
        operacion = "suma"
        digitoDisplay.set(resultado)

# -----------Funcion Total------------


def total():
    global resultado
    if(resultado+float(digitoDisplay.get())).is_integer:
        digitoDisplay.set(int(resultado+float(digitoDisplay.get())))
        resultado = 0
    else:
        digitoDisplay.set(resultado+float(digitoDisplay.get()))
        resultado = 0


# ---------Primera Fila-------------
boton7 = Button(miFrame, text="7", width=5,
                command=lambda: pulsacionesTeclas("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=5,
                command=lambda: pulsacionesTeclas("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=5,
                command=lambda: pulsacionesTeclas("9"))
boton9.grid(row=2, column=3)
botondiv = Button(miFrame, text="/", width=5)
botondiv.grid(row=2, column=4)

# ---------Segunda Fila-------------

boton4 = Button(miFrame, text="4", width=5,
                command=lambda: pulsacionesTeclas("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=5,
                command=lambda: pulsacionesTeclas("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=5,
                command=lambda: pulsacionesTeclas("6"))
boton6.grid(row=3, column=3)
botonmult = Button(miFrame, text="X", width=5)
botonmult.grid(row=3, column=4)

# ---------Tercera Fila-------------

boton1 = Button(miFrame, text="1", width=5,
                command=lambda: pulsacionesTeclas("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=5,
                command=lambda: pulsacionesTeclas("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=5,
                command=lambda: pulsacionesTeclas("3"))
boton3.grid(row=4, column=3)
botonresta = Button(miFrame, text="-", width=5)
botonresta.grid(row=4, column=4)

# ---------Cuarta Fila-------------

boton0 = Button(miFrame, text="0", width=5,
                command=lambda: pulsacionesTeclas("0"))
boton0.grid(row=5, column=1)
botoncoma = Button(miFrame, text=".", width=5,
                   command=lambda: pulsacion_coma())
botoncoma.grid(row=5, column=2)
botonigual = Button(miFrame, text="=", width=5, command=lambda: total())
botonigual.grid(row=5, column=3)
botonsum = Button(miFrame, text="+", width=5,
                  command=lambda: suma(digitoDisplay.get()))
botonsum.grid(row=5, column=4)


raiz.mainloop()
