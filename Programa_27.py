def prog_27():
    print("*********************¨*********************")
    print("DETERMINAR EL TIPO DE LICENCIA DE CONDUCIR")
    print("*******************************************")
    edad = int(input("Ingrese su edad: "))

    if edad >= 16 and edad <= 17:
        print("Licencia de menor")
    elif edad >= 18 and edad <= 65:
        print("Licencia de adulto")
    else:
        print("Licencia de adulto mayor")
