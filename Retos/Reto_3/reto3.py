personas = list(input().replace(" ","").upper())

Comparacion = []
ListaContador = []
letrasRepetidas= []
i=0
contador = 0

for letra in personas:
    Comparacion.append(letra)
    if letra == Comparacion[i-1]: 
        contador += 1
        if letra not in letrasRepetidas:
            letrasRepetidas.append(letra)
        if i==len(personas) - 1:           
            ListaContador.append(contador)
    elif letra != Comparacion[i-1]: 
        ListaContador.append(contador)
        letrasRepetidas.append(letra)
        contador = 1
        if i==len(personas) - 1:    
            ListaContador.append(1)
    i += 1
    
CadenaletrasRepetidas = ' '.join(letrasRepetidas)
print(CadenaletrasRepetidas)
MapListaContador = list(map(str,ListaContador))
CadenaListaContador= ' '.join(MapListaContador)
print(CadenaListaContador)
