def prog_14():
    print("**************************************")
    print("DETERMINAR SI UN CARACTER ES UNA VOCAL")
    print("**************************************")
    letra = input("Digite una letra: ")

    vocales = 'a','e','i','o','u','A','E','I','O','U'

    if len(letra) == 1 and letra in vocales:
        print("Es una vocal")
        
    else:
        print("No es una vocal")
        
    print("Fin de programa")
