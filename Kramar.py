while True:
	print("Enter matrix:\n")
	a = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(3):
		for j in range(3):
			a[i][j] = int(input())
	b1 = int(input("Enter result 1: "))
	b2 = int(input("Enter result 2: "))
	b3 = int(input("Enter result 3: "))
	print("\n")
	d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
	if d ==0:
		print("d =0")
		continue
	d1 = b1*a[1][1]*a[2][2] + b3*a[0][1]*a[1][2] + b2*a[0][2]*a[2][1] - b3*a[1][1]*a[0][2] - b1*a[1][2]*a[2][1] - b2*a[0][1]*a[2][2]
	d2 = a[0][0]*b2*a[2][2] + b1*a[1][2]*a[2][0] + a[0][2]*a[1][0]*b3 - a[0][2]*b2*a[2][0] - a[0][0]*a[1][2]*b3 - b1*a[1][0]*a[2][2]
	d3 = a[0][0]*a[1][1]*b3 + a[0][1]*b2*a[2][0] + b1*a[1][0]*a[2][1] - b1*a[1][1]*a[2][0] - a[0][0]*b2*a[2][1] - a[0][1]*a[1][0]*b3
	print("d =",d)
	print("d1 =",d1)
	print("d2 =",d2)
	print("d3 =",d3)
	print("\n\n")
	print("x1 =",d1/d)
	print("x2 =",d2/d)
	print("x3 =",d3/d)
	print("\n\n")