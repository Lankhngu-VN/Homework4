chuoi = input()
length = 0
for a in chuoi:
    length += 1
so_tu = 0

for i in range(length):
    if chuoi[i] != ' ':
        if i == 0 or chuoi[i-1] == ' ':
            so_tu += 1
print(so_tu)