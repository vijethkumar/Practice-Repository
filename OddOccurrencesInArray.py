N = [1,2,3,6,3,2,1,6,7,4,7,9,4,8,0,9,0]
vijeth = {}
for i in N:
    vijeth[i] = 0
for i in N:
    vijeth[i] = vijeth[i] + 1

vijeth_keys=[]
vijeth_values = []
for key,values in vijeth.items():
    vijeth_keys.append(key)
    vijeth_values.append(values)
# vi = vijeth_values.index(1)
print(vijeth_keys[vijeth_values.index(1)])

