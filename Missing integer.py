N = [1]
N.sort()
dictA = {}
loc =0
N_values=[]
N_keys=[]
for i in range(1,len(N)+2):
    dictA[i]=0
print(dictA)

for i in N:
    dictA[i]+=1

print(dictA)

for k,v in dictA.items():
    N_values.append(v)
    N_keys.append(k)

for i in range(len(N_values)):
    if N_values[i]== 0:
        loc = i

print(N_keys[loc])




# for i in range(len(N)-1):
#     if N[i+1] != N[i] + 1:
#         print(N[i]+1)



