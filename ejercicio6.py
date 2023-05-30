lista = []

pross = True 
while pross:
    try:
        print("Ingrese numeros\nPulse 0 para terminar")
        num = int(input())
        if num > 0 and num <= 100:
            lista.append(num)
            lista.sort()
            print(lista)      
            print("")
        
        elif num == 0:
            pross = False;
        
        else:
            print("SOLO NUMEROS DEL 1 AL 100")
        
    except ValueError:
        print("INGRESE UN VALOR VALIDO")