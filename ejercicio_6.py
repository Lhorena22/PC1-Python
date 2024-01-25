edad = int(input('Ingrese su edad: '))
if edad < 4:
    print('El ingreso es gratuito')
elif edad >= 4 and edad <= 18:
    print('El precio de la entrada es de $5')
elif edad > 18:
    print('El precio de la entrada es de $10')