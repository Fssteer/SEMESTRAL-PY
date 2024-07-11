def prog_2():
    print("**************************")
    print("CALCULO DEL IMPUESTO DE UN PRODUCTO")
    print("**************************")
    precio = float(input("Digite precio  del producto:"))
    cantidad = float(input("Digite cantidad de productos:"))
    p1 = precio *  cantidad
    p2 = p1 *  0.10
    p3 = p1 + p2
    print("Calculo de impuesto es:",p3)