def prog_45():
    print("**********************")
    print("MULTIPLOS DE UN NUMERO")
    print("**********************")
  
    numero = int(input("Ingrese un número entero positivo: "))

    contador = 1

    while contador <= 10:
     
      multiplo = numero * contador

      print(f"{numero} x {contador} = {multiplo}")

      contador += 1