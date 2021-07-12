'''
se debe crear un módulo llamado libreriap76 que contenga las siguientes funciones:

1.) crear una función llamada repetidas que retorne en una lista los valores que se encuentran repetidos 
    en una lista de entrada
2.) una función reverse(lista) que dada una lista retorne una copia inversa de la lista 
3.) una función llamada elementoen(elementos, indices) que dadas las listas elementos y la lista indices
    retorne la lista de elementos que se encontraban en los indices 
4.) una función llamada enambos(lista1, lista2) la cual dadas dos listas retorne una lista de elementos 
    que están en la lista uno y en la lista dos


'''

'''
lista de ejemplo para repetidas 
['reloj','arete','reloj','anillo','collar','colgante','colgante','anillo','arete','reloj']
'''
#cadena=input('ingrese la lista para buscar las repetidas: ')
def repetidas(lista):
    longitud=len(lista)
    j=1
    inicial=0
    repeti=[]
    norevi=[]
    for i in range(longitud):
        for j in range(longitud):
            if(lista[i]==lista[j] and lista[i] not in repeti):
                repeti.append(lista[i])
    print(repeti)        
cadena=['reloj','arete','reloj','anillo','collar','colgante','colgante','anillo','arete','reloj']
repetidas(cadena)
