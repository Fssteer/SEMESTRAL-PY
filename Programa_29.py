# Verificar si un nombre es corto, mediano o largo
def prog_29():
    print("*************************************************")
    print("VERIFICAR SI UN NOMBRE ES CORTO, MEDIANO O LARGO")
    print("*************************************************")
    nombre = input("Ingrese su nombre: ")

    largo_nombre = len(nombre)

    if largo_nombre < 5:
        print(f"El nombre {nombre} es corto.")
    elif largo_nombre <= 8:
        print(f"El nombre {nombre} es mediano.")
    else:
        print(f"El nombre {nombre} es largo.")
