import Programa_1, Programa_2, Programa_3, Programa_4, Programa_5, Programa_6, Programa_7, Programa_8, Programa_9, Programa_10
import Programa_11, Programa_12, Programa_13, Programa_14, Programa_15, Programa_16, Programa_17, Programa_18, Programa_19, Programa_20
import Programa_21, Programa_22, Programa_23, Programa_24, Programa_25, Programa_26, Programa_27, Programa_28, Programa_29, Programa_30
import Programa_31, Programa_32, Programa_33, Programa_34, Programa_35, Programa_36, Programa_37, Programa_38, Programa_39, Programa_40
import Programa_41, Programa_42, Programa_43, Programa_44, Programa_45, Programa_46, Programa_47, Programa_48, Programa_49, Programa_50
def main():
    while True:
        print("\n\n😄==== Menú ====😄")
        print("1-10. Elija un programa diagrama de flujo")
        print("11-20. Elija un programa sentencia if")
        print("21-30. Elija un programa sentencia else")
        print("31-40. Elija un programa bucle While")
        print("41-50. Elija un programa bucle for")
        print("q. Salir")
        choice = input("Elige una opción: ")
        print("\n")

        match choice:
            case "1":
                Programa_1.prog_1()
            case "2":
                Programa_2.prog_2()
            case "3":
                Programa_3.prog_3()
            case "4":
                Programa_4.prog_4()
            case "5":
                Programa_5.prog_5()
            case "6":
                Programa_6.prog_6()
            case "7":
                Programa_7.prog_7()
            case "8":
                Programa_8.prog_8()
            case "9":
                Programa_9.prog_9()
            case "10":
                Programa_10.prog_10()
            case "11":
                Programa_11.prog_11()
            case "12":
                Programa_12.prog_12()
            case "13":
                Programa_13.prog_13()
            case "14":
                Programa_14.prog_14()
            case "15":
                Programa_15.prog_15()
            case "16":
                Programa_16.prog_16()
            case "17":
                Programa_17.prog_17()
            case "18":
                Programa_18.prog_18()
            case "19":
                Programa_19.prog_19()
            case "20":
                Programa_20.prog_20()
            case "21":
                Programa_21.prog_21()
            case "22":
                Programa_22.prog_22()
            case "23":
                Programa_23.prog_23()
            case "24":
                Programa_24.prog_24()
            case "25":
                Programa_25.prog_25()
            case "26":
                Programa_26.prog_26()
            case "27":
                Programa_27.prog_27()
            case "28":
                Programa_28.prog_28()
            case "29":
                Programa_29.prog_29()
            case "30":
                Programa_30.prog_30()
            case "31":
                Programa_31.prog_31()
            case "32":
                Programa_32.prog_32()
            case "33":
                Programa_33.prog_20()
            case "34":
                Programa_34.prog_34()
            case "35":
                Programa_35.prog_35()
            case "36":
                Programa_36.prog_36()
            case "37":
                Programa_37.prog_37()
            case "38":
                Programa_38.prog_20()
            case "39":
                Programa_39.prog_39()
            case "40":
                Programa_40.prog_40()
            case "41":
                Programa_41.prog_41()
            case "42":
                Programa_42.prog_42()
            case "43":
                Programa_43.prog_43()
            case "44":
                Programa_44.prog_44()
            case "45":
                Programa_45.prog_45()
            case "46":
                Programa_46.prog_46()
            case "47":
                Programa_47.prog_47()
            case "48":
                Programa_48.prog_48()
            case "49":
                Programa_49.prog_49()
            case "50":
                Programa_50.prog_50()
            case "q":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()