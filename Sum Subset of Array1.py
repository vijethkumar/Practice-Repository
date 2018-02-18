A =[0,0,0]
Vijeth_Size = 0
Vijeth_Size1 = 0

Sum_A = 0
for x in range(len(A)):
    Sum_A += A[x]
if Sum_A >= 0:
    print(len(A))
else:
    for i in range(len(A)):
        for j in range(len(A)):
            A1 = A[i:j]
            Sum_A1 = 0
            for k in range(len(A1)):
                Sum_A1 += A1[k]
            if Sum_A1 >= 0 :
                Vijeth_Size1=j-i
            if Vijeth_Size1 > Vijeth_Size:
                Vijeth_Size = Vijeth_Size1

    print(Vijeth_Size)
