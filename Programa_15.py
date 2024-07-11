def prog_15():
    print("**********************************************")
    print("VERIFICAR SI UNA PALABRA TIENE MAS DE 5 LETRAS")
    print("**********************************************")
    palabra = input("Digite una palabra: ")

    if len(palabra) > 5:
        print("La palabra que digito tiene mas de 5 letras")
    if len(palabra) ==5:
        print("La palabra que digito tiene 5 letras")
    else:
        print("La palabra que digito tiene menos de 5 letras")

    print("Fin de Programa")
