def find_threes (v):
	numero=[]
	numerom=[]
	n=0
	c=0
	suma=0
	nu=int(input("cuantos numero quieres agregar a la lista "))
	while (n<nu):
		h=int(input("dame un numero "))
		numero.append(h)
		n=n+1
	for k in range (0,nu):
		y=numero[k]%3
		if (y==0):
			numerom.append(numero[k])
			c=c+1
	for e in range(0,c):
		suma=suma+numerom[e]
	print("Los numero dibisibles entre 3 son: ",numerom)
	print("La suma de los numero dibisibles entre 3 es: ", suma)


v=0
find_threes(v)
