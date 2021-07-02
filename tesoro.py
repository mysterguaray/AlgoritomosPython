plark=int(input())
helios=int((2*plark)+4)
lumina=int((helios+plark)/5)

def clasificacion(monedas):
	if monedas>=0 and monedas<=20:
		clasif="Uno"
	elif monedas>=21 and monedas<=30:
		clasif="Dos"	
	elif monedas>=31 and monedas<=50:
		clasif="Tres"
	elif monedas>50:
		clasif="Cuatro"
	return(clasif)


print (str(plark)+" "+str(helios)+" "+str(lumina))
print (clasificacion(lumina))