A = int(input())
a = 1
b = 1
while b <= A:
    tiep = a + b
    a = b
    b = tiep
print(a)