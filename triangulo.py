def triangle (n):
	x=n
	for x in range (1,n+1):
		print ("T"*x)
		y=x
	while (y>0):
		print("T"*(y-1))
		y=y-1



n=int(input("Dame un numero "))
triangle(n)