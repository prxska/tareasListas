
nombres = []

print("Ingrese un nombre")
nombre1 = input()
nombres.append(nombre1)
print("Ingrese un nombre")
nombre2 = input()
nombres.append(nombre2)
print("Ingrese un nombre")
nombre3 = input()
nombres.append(nombre3)

nombres.sort() 

# SE USA LA FUNCION 'MAX' EL 'KEY=LEN' COMPARA LAS DIMENSIONES DE LAS CADENAS DE TEXTO
# AL USAR LA FUNCION 'MAX' BUSCARA LA EL STRING MAS LARGO

nombreLargo = max(nombres, key=len) 

print("")
print("El nombre mas largo es:" , nombreLargo)