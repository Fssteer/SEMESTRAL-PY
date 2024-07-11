def prog_10():
    print("**************************")
    print("CALCULAR SALARIO MENSUAL")
    print("**************************")
    def calcular_salario(horas_trabajadas, salario_por_hora, horas_extra):
        salario_total = horas_trabajadas * salario_por_hora
        salario_extra = horas_extra * salario_por_hora * 2
        salario_mensual_total = salario_total + salario_extra
        return salario_mensual_total, salario_extra
    
    horas_trabajadas = float(input("Digite las horas trabajadas en el mes: "))
    salario_por_hora = float(input("Digite el salario por hora: "))
    horas_extra = float(input("Dijite el número de horas extra trabajadas: "))
    
    salario_total, monto_extra = calcular_salario(horas_trabajadas, salario_por_hora, horas_extra)
    
    print("El salario mensual es:", salario_total)