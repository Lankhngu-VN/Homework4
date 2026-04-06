n = int(input())
if n < 0:
    print("Nhap so nguyen duong")
else:
    temp = n
    while temp > 1:
        temp /= 2
        if temp == 1:
            print(f"{n} la so nguyen duong co dang 2^k")
            break
    else:
        print(f"{n} khong la so nguyen duong co dang 2^k")
