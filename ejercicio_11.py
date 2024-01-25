lista = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = []
for i in lista:
    if i not in lista_procesada:
        lista_procesada.append(i)
print(lista_procesada)