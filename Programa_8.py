def prog_8():
    print("**************************")
    print("MULTIPLOS")
    print("**************************")
    def  resolver_ecuacion(ecuacion, x):
        resultado = eval(ecuacion)
        return resultado
    
    # Ecuaciones
    ecuacion_A = "20 -( 7 * x)"
    ecuacion_B = " (- 7 * x) + 2 - (10*x) + 5"
    ecuacion_C = "(4*x) + 4 + (9*x )+ 18"
    ecuacion_D = "(6*x) - 5 +(8*x )+2"
    ecuacion_E = "((5*x) + 78)/28"
    ecuacion_F ="(((6*x)-7)/4)+((3 * x)-5)/7"
    
    # Definir el valor de x
    valor_x = 3
    
    # Resolver las ecuaciones
    resultado_A = resolver_ecuacion(ecuacion_A, valor_x)
    resultado_B = resolver_ecuacion(ecuacion_B, valor_x)
    resultado_C = resolver_ecuacion(ecuacion_C, valor_x)
    resultado_D = resolver_ecuacion(ecuacion_D, valor_x)
    resultado_E = resolver_ecuacion(ecuacion_E, valor_x)
    resultado_F = resolver_ecuacion(ecuacion_F, valor_x)
    
    # Mostrar los resultados
    print("Resultado de la ecuación A para x =", valor_x, ":", resultado_A)
    print("Resultado de la ecuación B para x =", valor_x, ":", resultado_B)
    print("Resultado de la ecuación C para x =", valor_x, ":", resultado_C)
    print("Resultado de la ecuación D para x =", valor_x, ":", resultado_D)
    print("Resultado de la ecuación E para x =", valor_x, ":", resultado_E)
    print("Resultado de la ecuación F para x =", valor_x, ":", resultado_F)