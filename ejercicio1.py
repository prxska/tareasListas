
tabla = []

try:

    print("Ingrese un numero:")
    numero = int(input())
    for hola in range(1, 11):
        tabla.append(numero * hola)
    print(tabla)

except ValueError:
    print("Ingrease un valor valido")