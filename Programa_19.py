def prog_19():
    print("**************************************************")
    print("DETERMINAR SI UN CARACTER ES UNA LETRA O UN DIGITO")
    print("***************************************************")
    vocales = ["a", "e", "i", "o", "u" , "A", "E", "I", "O", "U"]

    caracter = input("Introduce un carácter: ")

    if caracter.isdigit():
        print(f"El carácter '{caracter}' es un dígito.")
        
    elif caracter in vocales:
        print(f"El carácter '{caracter}' es una vocal.")
        
    else:
        print(f"El carácter '{caracter}' no es ni una vocal ni un dígito.")

    print("Fin de programa")
