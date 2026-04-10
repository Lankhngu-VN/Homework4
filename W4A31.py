chuoi = input()
hoa = 0
thuong = 0
so = 0
for i in chuoi:
    if i.isupper():
        hoa +=1
    elif i.islower():
        thuong +=1
    elif i.isdigit():
        so +=1
print(f'So ki tu hoa: {hoa}')
print(f'So ki tu thuong: {thuong}')
print(f'So ki tu so: {so}')