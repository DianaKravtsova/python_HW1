import numpy as np

n = int(input("введите n\n"))

s = np.zeros((n,n))
k = 1

for i in range(n):
    s[0][i] = k
    k += 1
for i in range(1,n,1):
    s[i][n-1] = k
    k += 1
for i in range(2, n, 1):
    s[n-1][n-i]=k
    k +=1
for i in range(1, n, 1):
    s[n-i][0] = k
    k += 1

i = 1
j = 1
while k < n**2:
    while s[i][j+1] == 0:
        s[i][j] = k
        k += 1
        j += 1
    while s[i+1][j] == 0:
        s[i][j] = k
        k += 1
        i +=1
    while s[i][j-1] == 0:
        s[i][j] = k
        k += 1
        j -= 1
    while s[i-1][j] == 0:
        s[i][j] = k
        k += 1
        i -= 1

for i in range(n):
    for j in range(n):
        if s[i][j] == 0:
            s[i][j] = k
print(s)


