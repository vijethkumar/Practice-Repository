A=[]
N=9
Result = [3,4,5,1,2]
temp=0
if not A:
    print(A)
else:
    for i in range(N):
        temp=A.pop()
        A.insert(0,temp)

    print(A)

