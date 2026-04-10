n = int(input())
if n > 1000 and n < 0:
    print("Nhap lai n")
else:
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)