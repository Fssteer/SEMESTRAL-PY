def prog_40():
    print("*********************")
    print("TABLA DE MULTIPLICAR")
    print("*********************")
    print ("/Tabla de multiplicar ciclo for/")

    numero = int (input("ingrese su numero entero positivo: "))
    for i  in range (1,12):
        respuesta = numero * i
        print("------------------------------------------------")
        print (f"{numero} x {i} =  {respuesta}")
    print("-------------------------------------------------")
