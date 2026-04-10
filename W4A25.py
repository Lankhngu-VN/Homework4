a = 0
b = 0
print("Nhập vào một dãy số nguyên (nhập -1 để kết thúc):")
while True:
    n = int(input())
    if n >a:
        a = n
    if n < b:
        b = n
    if n == -1:
        break
print(f"Số lớn nhất là: {a}")
print(f"Số nhỏ nhất là: {b}")