A = [2,3,6]
A.sort()

Max = A[len(A)-1]
if Max <= 0:
    print('1')
else:
    if A[0] <=0:
        Min = A[0]
    else:
        Min = 1
    print(Max)
    dictA = {}
    Solved = 0

    for i in range(Min,Max+1):
        dictA[i]= 0

    print(dictA)

    for i in A:
        dictA[i] = dictA[i]+ 1

    for key ,value in dictA.items():
        if value == 0  and key > 0:
            Solved = key
            break
    if Solved ==0:
        print(Max+1)
    else:
        print(Solved)
