def prog_44():
    print("******************************")
    print("CONVERTIR DE DECIMAL A BINARIO")
    print("******************************")
    numero_decimal = int(input("Ingrese un número entero positivo: "))

    binario = ""

    while numero_decimal > 0:

      residuo = numero_decimal % 2

      binario = str(residuo) + binario

      numero_decimal //= 2

    binario_invertido = binario[::-1]
    
    print("El número binario es:", binario_invertido)

    print("FIN DEL PROGRAMA")

