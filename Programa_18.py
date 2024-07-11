def prog_18():
    print("***************************************")
    print("VERIFICAR SI UN NUMERO ESTA EN SU RANGO")
    print("***************************************")
    numero = float(input("Ingresa un número: "))
    if 1 <= numero <= 100:
        print("El numero está entre 1 y 100.")
    else:
        print("El numero no está entre 1 y 100.")