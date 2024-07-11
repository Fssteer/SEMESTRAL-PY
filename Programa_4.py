def prog_4():
    print("**************************")
    print("HALLAR EL PERÍMETRO DE UN RECTÁNGULO")
    print("**************************")

    
    AB = float(input("Longitud del lado AB: "))
    BC = float(input("Longitud del lado BC: "))
    CD = float(input("Longitud del lado CD: "))
    DA = float(input("Longitud del lado DA: "))

    p = 2 * (AB + BC + CD + DA)

    print("El perímetro del rectángulo es:", p)
