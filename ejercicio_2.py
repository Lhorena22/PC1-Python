costoComida = int(input('Ingrese el costo de su comida: '))
porcentaje = int(input('Ingrese el porentaje de propina que desea dejar al mesero: '))
monto = round(costoComida * (porcentaje/100),2)
print(f"El monto de propina es: ${monto}")