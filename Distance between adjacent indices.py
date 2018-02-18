A = [1,4,7,3,3,5,6,7,8,9,10,11]
Output=0
sum = 10
Output_list=[]
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if abs(A[i]-A[j]) == 1 :
            Output=j-i
            Output_list.append(Output)
if not Output_list:
    Output=0
    print(Output)
else:
    Output_list.sort()
    print(Output_list[0])
