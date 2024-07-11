def prog_30():
    print("******************************")
    print("CALCULAR LA TARIFA DE UN TAXI")
    print("******************************")
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))

    if distancia <= 10:
        tarifa = distancia * 2.50
    else:
        tarifa = 10 * 2.50 + (distancia - 10) * 2.00

    print(f"La tarifa del taxi es: ${tarifa:.2f}")
