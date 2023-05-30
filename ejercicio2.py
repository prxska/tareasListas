

lista = []

try:
    pross = True;
    while pross:    
        print("Ingrese un numero\nPulse 0 para terminar y mostrar lista")
        
        num = int(input())
        
        if num != 0:
            lista.append(num)

        else:
            pross = False
            lista.sort()
            print(lista)
        
except ValueError:
    print("Inserte un caracter valido")