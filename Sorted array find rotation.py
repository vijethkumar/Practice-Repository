a = [7, 9, 11, 12, 5, 6]

small = a[0]

for i in range(len(a)):
    if a[i] < small:
        small = a[i]
        index=i

# for i in range(len(a)):
#     if a[i] == small:
#         index = i
print(small)
print(index)
