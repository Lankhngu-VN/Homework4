n = int(input())
S = 0
k = 0
while S + (k + 1) <= n:
    k += 1
    S += k
print(k)

