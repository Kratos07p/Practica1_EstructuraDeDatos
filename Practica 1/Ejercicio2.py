#Ingresar 2 numeros y mostrar quien es el menor y quien es el menor
num1 =float(input("Ingrese el primer numero: "))
num2 =float(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor a {num2}, el mayor es el primer numero")

elif num2 > num1:
    print(f"El numero {num2} es mayor a {num1}, el mayor es el segundo numero")

else:
    print(f"El numero {num1} y el numero {num2} son iguales y ninguno es mayor al otro")