import json
joyasTienda = input()
faltan=input()
diccionario = json.loads(joyasTienda)
lista=faltan.split(" ")
valor=0
puedeComprar=[]
for i in range(len(lista)):
    if lista[i] in diccionario.keys():
        puedeComprar.append(lista[i])
        valor+= diccionario.get(lista[i])
listafinal = " ".join(puedeComprar)
print(valor)
print(listafinal)