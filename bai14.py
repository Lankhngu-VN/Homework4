chuoi = input()
chuoi_moi = ''
for i in chuoi:
    if i.islower():
        chuoi_moi += i.upper()
    elif i.isupper():
        chuoi_moi += i.lower()
    else:
        chuoi_moi += i
print(chuoi_moi)