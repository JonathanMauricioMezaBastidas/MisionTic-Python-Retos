# reto pizzeria
import json

lista=input()
listaj=json.loads(lista)
ingredientes=input()
ingredientes=ingredientes.split(" ")
ingredientes=list(ingredientes)

i=0
total=0
ingredientesTotal=[]
ingredientesOrden=[]

for key in listaj.keys():
    for i in range(len(ingredientes)):
      if ingredientes[i] in key:
          total=total+listaj[key]
          ingredientesTotal.append(key)
          i=i+1

    i=0

for c in ingredientes:
  if c in ingredientesTotal:
    ingredientesOrden.append(c)          
    
  
ingredientesOrden=" ".join(map(str,ingredientesOrden))
print(total)
print(ingredientesOrden)
