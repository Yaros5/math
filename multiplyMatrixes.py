while True:
  print("Enter matrix A size:\n\n")
  m1 = int(input("Rows = "))
  n1 = int(input("Columns = "))
  print("\n\nEnter matrix B size:\n\n")
  m2 = int(input("Rows = "))
  n2 = int(input("Columns = "))
  if(n1 != m2):
    print("\n\nNumber of columns of matrix A isn't equal to number of rows of matrix B\n\n")
    continue
  A = []
  B = []
  C = []
  for i in range(m1*n2):
    C.append(0)
  print("\n\nEnter matrix A:\n\n")
  for i in range(m1*n1):
    A.append(int(input()))
  print("\n\nEnter matrix B:\n\n")
  for i in range(m2*n2):
    B.append(int(input()))
  print("\n\n")
  for i in range(m1):
    for j in range(n2):
      for k in range(n1):
        for l in range(m2):
          C[i*m1+j] += A[i*m1+k]*B[l*m2+j]
  for i in range(m1*n2):
        print(C[i], end=' ')
        if n2/i == 0:
          print("\n")
  print("\n\n")
