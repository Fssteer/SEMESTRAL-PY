def prog_7():
    print("**************************")
    print("RESOLVER LAS ECUACIONES DANDO EL VALOR DE X")
    print("**************************")
    a = 2
    b = 5
    c = 3
    aux = 0
    
    a = a + 3
    b = 5 * a
    c = b
    aux = c
    a = b + c
    b = aux / c
    c = (a + b) * aux
    
    print(a, b, c, aux)