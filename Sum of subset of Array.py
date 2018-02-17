# 1  find the sum of all the array elements

vijeth_list = [1,1,1,1,-1] # [1, 1, -1, -1, -1, -1, -1, 1, 1]
LengthOfList = len(vijeth_list)
# Sum = 0
# for i in range(len(vijeth_list)):
#     Sum += vijeth_list[i]
# print(Sum)

def sum_of_array(list1):
    SumR = 0
    for i in range(len(list1)):
        SumR += list1[i]
    return SumR
Size = 0
Size1 = 0
for i in range(LengthOfList):
    for j in range(i,LengthOfList):


        if sum_of_array(vijeth_list[i:j]) >= 0:
            Size1 = j-i
        if Size1 > Size :
            Size = Size1

print(Size)
print(LengthOfList)

