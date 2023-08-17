#Ingresar 5 números y visualizarlos ordenados de forma ascendente
numeros = []
for i in range(5):
    num = float(input("Ingrese el numero: "))
    numeros.append(num)

n = len(numeros)
for i in range(n):
    for j in range(i + 1 , n):
        if numeros[i] > numeros[j]:
            intercambiar = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = intercambiar

for num in numeros:
    print(f"El orden es el siguiente: {num}")
