print("enter a integer:")
N = int(input())
string = str(bin(N))
# print(string)
binary='{:b}'.format(N)
print(binary)
# print(binary[0])
len = len(binary)
# print(len)
Z = 0
F = 0
for i in binary:
     if i == "0":
         Z += 1
     else:
         if Z > F :
             F = Z
             Z = 0
         else:
             Z = 0
if Z > F :
    F = Z

print(F)
