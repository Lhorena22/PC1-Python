num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
print("""MENU:
a) Mostrar una suma de los dos números
b) Mostrar una resta de los dos números (el primero menos el segundo)
c) Mostrar una multiplicación de los dos números""")
opcion = input('Elija una de las tres opciones: ')
if opcion == 'a':
    print(num1 + num2)
elif opcion == 'b':
    print(num1 - num2)
elif opcion == 'c':
    print(num1 * num2)
else:
    print("Opcion no valida")