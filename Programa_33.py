def prog_33():
    print("**********************************")
    print("DIBUJAR UN TRIANGULO DE ASTERISCOS")
    print("**********************************")
    ("/Dibujar un triángulo de asteriscos/")
    for altura in range(1, 6):
      espacios = altura - 1
      for _ in range(espacios):
        print(" ", end="")
      for _ in range(altura):
        print("*", end="")
      print() 
