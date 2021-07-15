def funcion_decoradora(funcion_a_decorar):
    def hago_el_trabajo(*args, **kwargs):
        print("A continuacion voy a realizar un calculo, cuyo resultado es: ")
        funcion_a_decorar(*args, **kwargs)
        print("----Ya termine mi trabajo----")

    return hago_el_trabajo
 # ddddddddddddddddd


@funcion_decoradora
def suma(nro1, nro2, nro3):
    print(nro1+nro2+nro3)


@funcion_decoradora
def resta(nro1, nro2):
    print(nro1-nro2)


@funcion_decoradora
def otra(saludo):
    print("Yo solo uso 1 parametro " + saludo)


@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


suma(5, 7, 100)  # 3 parametros
resta(20, 13)  # 2 parametros
otra("Un abrazo")  # 1 parametro
# argumentos con clave:valor. Lo toma el **kwargs
potencia(base=5, exponente=3)
