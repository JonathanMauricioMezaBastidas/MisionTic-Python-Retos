# Author: [Jonathan Meza](https://github.com/JonathanMeza0107)
j=input()
k=input()
g=input()
x=''

def libreta(x):
	contador_j=0
	contador_k=0
	for letra in g:
		if letra in j:
			contador_j+=1
		if letra in k:
			contador_k+=1
		if contador_j==contador_k:
			x+='L'
		elif contador_j>contador_k:
			x+='J'
		elif contador_k>contador_j:
			x+='K'
	return x	
			
if __name__ == '__main__':
	print(libreta(x))