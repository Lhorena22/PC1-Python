hora = input('Ingrese una hora del día: ')
indice = hora.index(':')
primario = int(hora[:indice])
secundario = int(hora[indice+1:])
if (7 <= primario < 8) or (primario == 8 and secundario == 00):
    print("Es hora de desayunar.")
elif (12 <= primario < 13) or (primario == 13 and secundario == 00):
    print("Es hora de almorzar.")
elif (18 <= primario < 19) or (primario == 19 and secundario == 00):
    print("Es hora de cenar.")