chuoi = input()
first_char = ''
for i in range(len(chuoi)):
    if chuoi[i] != ' ':
        first_char = chuoi[i]
        break
print(first_char)
