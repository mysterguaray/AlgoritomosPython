def categorias(lista_categoria_joyas):
    repeti=[]
    for i in lista_categoria_joyas:
            if(lista_categoria_joyas.count(i)>=1 and i not in repeti):
                repeti.append(i)
    return(repeti)        
#cadena=['reloj','arete','reloj','anillo','collar','colgante','colgante','anillo','arete','reloj']
#result=categorias(cadena)
#print(result)

def faltandecategoria(referencias, categorias, categoria):
    longitud=len(categorias)
    encontradas=[]
    for i in range(longitud):
        if categoria==categorias[i]:
            encontradas.append(i)
    rangoref=len(referencias)
    faltan=[]
    for j in encontradas:
        for k in range(rangoref):
            if j==referencias[k]:
                faltan.append(j)
    return(faltan)
#cadena=['reloj','arete','reloj','anillo','collar','colgante','colgante','anillo','arete','reloj','arete', 'collar', 'arete']
#refe=[1,3,6,8]
#result=faltandecategoria(refe,cadena,'arete')
#print(result)

def notengo(listasparrow, listabarbanegra):
    longbarba=len(listabarbanegra)
    barbanotiene=[]
    for i in listasparrow:
        if (i not in listabarbanegra and i not in barbanotiene):
            barbanotiene.append(i) 
    return(barbanotiene)
#listasparrow=[3,5,7,10,15,16]
#listabarba=[4,10,5,8]
#resultado=notengo(listasparrow,listabarba)
#print(resultado)

def intercambiables(listasparrow, listabarbanegra):
    contadorbrb=0
    contadorsp=0
    for i in listabarbanegra:
        if(i not in listasparrow):
            contadorbrb+=1
    for i in listasparrow:
        if i not in listabarbanegra:
            contadorsp+=1
    if contadorbrb>contadorsp:
        return(int(contadorsp))
    else:
        return(contadorbrb)
#sparrow=[3,5,7,10,15,16]
#barbanegra=[4,10,5,8]
#resultado=intercambiables(sparrow,barbanegra)
#print(resultado)

sparrow=[4,2]
barbanegra=[3,5,0]
resultado=intercambiables(sparrow,barbanegra)
print(resultado)





