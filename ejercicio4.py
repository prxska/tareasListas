

lista = []

pross = 1 
while pross:
    try:
        for hola in range(20):
            num = int(input('Digite um número: '))
            if num > 0 and num <= 100:
                lista.append(num)
            else:
                print("SOLO NUMEROS DE 1 AL 100")
        print(lista)
        pross = False; 
    except ValueError:
        print("Ingrese caracteres validos")