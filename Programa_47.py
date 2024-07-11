def prog_47():
    print("**************************")
    print("SUMAR DIGITOS DE UN NUMERO")
    print("**************************")

    numero = int(input("Ingrese un número entero: "))

    suma_digitos = 0

    while numero > 0:
      digito = numero % 10
      suma_digitos += digito
      numero //= 10

    print("La suma de los dígitos del número es:", suma_digitos)

    print("FIN DEL PROGRAMA")
