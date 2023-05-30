nombres =[]


try:
    pross = True;
    while pross:    
        print("Ingrese un nombre")
        nom = str(input())
        nombres.append(nom)
        print("Desea continuar? NO/SI")
        op = str(input())
        if op == "NO":
            nombreChico = min(nombres, key=len)
            nombres.remove(nombreChico)
            print(nombres)
            break
except ValueError:
    print("Ingrese un caracter")


