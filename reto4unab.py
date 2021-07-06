import os
os.system("cls")

print("TABLA DE ENTRENAMIENTOS")
print()
kmRecorridosPrimerDia=int(input("Digite el número de kilometros recorridos el primer día: "))
numerosDiasEntrenados=int(input("Digite el número de días entrenados: "))
print()

sumaTotal=0
cadaTresDias=0
restoDeDias=0
diccionario=[]
for i in range(numerosDiasEntrenados):
    diccionario1={}
    diccionario1.setdefault('Día' ,i+1)
    operacion=(kmRecorridosPrimerDia*2)+10
    if (diccionario1['Día'])%3==0:
        cadaTresDias=kmRecorridosPrimerDia/2
        diccionario1.setdefault('Km Recorridos',cadaTresDias)
        kmRecorridosPrimerDia=cadaTresDias
        print(kmRecorridosPrimerDia)
    elif (diccionario1['Día'])==1:
        diccionario1.setdefault('Km Recorridos',kmRecorridosPrimerDia)
    else:
        restoDeDias=operacion
        diccionario1.setdefault('Km Recorridos',restoDeDias)
        kmRecorridosPrimerDia=restoDeDias
    sumaTotal+=diccionario1['Km Recorridos']
    diccionario1.setdefault('Acumulado' ,sumaTotal)
    diccionario.append(diccionario1)

for i in diccionario:
    print(i)