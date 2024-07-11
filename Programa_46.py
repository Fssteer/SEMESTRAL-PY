def prog_46():
    print("****************************")
    print("SIMULAR UN CAJERO AUTOMATICO")
    print("****************************")

    pin_correcto = "1234"

    intentos = 0

    while intentos < 3:
     
      pin_ingresado = input("Ingrese su PIN: ")

      if pin_ingresado == pin_correcto:
        print("¡PIN correcto! Acceso concedido.")
        break  
      else:
        print("PIN incorrecto. Intentos restantes:", 3 - intentos - 1)
        intentos += 1  

    if intentos == 3:
      print("¡Cuenta bloqueada! Contacte a su banco.")
      
    print("FIN DEL PROGRAMA")
