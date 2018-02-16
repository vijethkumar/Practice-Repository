N = [1,2,3,6,3,2,1,6,7,4,7,9,4,8,0,9,0]
vijeth = {}
for i in N:
    vijeth[i] = 0
for i in N:
    vijeth[i] = vijeth[i] + 1

print(len(vijeth.keys()))
