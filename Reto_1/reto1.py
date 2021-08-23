def fR1(indice_vulnerabilidad):
	factorR1=indice_vulnerabilidad
	fR2=factorR1*2
	fR2= fR2-(-4)
	fR3=factorR1+fR2
	fR3=fR3/5
	fR3=int(fR3)
	print(factorR1,fR2,fR3)
	if fR3 >= 0 and fR3 <=20:
		print("uno")
	elif fR3 >= 21 and fR3 <=30:
		print("dos")		
	elif fR3 >= 31 and fR3 <=50:
		print("tres")
	else:
		print("cuatro")
	return ""

indice=int(input())
print(fR1(indice))
