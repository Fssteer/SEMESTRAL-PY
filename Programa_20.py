def prog_20():
    print("**********************")
    print("COMPARAR DOS NUMEROS")
    print("**********************")
    numero1 = float(input("Ingrese el primer número: "))

    numero2 = float(input("Ingrese el segundo número: "))

    if numero1 > numero2:
        print("El primer número es mayor.")
    elif numero1 < numero2:
        print("El segundo número es mayor.")
    else:
        print("Ambos números son iguales.")

    print("Fin de programa")
