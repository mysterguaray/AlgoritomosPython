sparrow=input("ingrese las letras de sparrow: ")
barbanegra=input("ingrese las letras de barbanegra: ")
juez=input("ingrese las letras del juez: ")

sp=0
brb=0
cadena=""
for i in juez:
    
    if i in sparrow:
        sp+=1
    if i in barbanegra:
        brb+=1
    
    if sp>brb:
        cadena=cadena +"S"
    elif brb>sp:
        cadena=cadena + "B"
    else:
        cadena=cadena + "I"
        
print(cadena)

