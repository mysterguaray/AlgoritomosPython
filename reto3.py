cadena=input("ingrese las letras: ")
cadena=cadena.replace(" ", "")
lista=list(cadena)
lista1=[]
lista2=[]
contador=1
rango=len(lista)

for i in range(0,len(lista)-1):
    if lista[i]==lista[i+1]:
          contador=contador+1
    else:
        lista2.append(contador)
        lista1.append(lista[i])
        contador=1
lista2.append(contador)
lista1.append(lista[rango-1])

listaA = " ".join(lista1)
listaB = " ".join(map(str, lista2))
print(listaA)    
print(listaB)

        




