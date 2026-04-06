n = int(input())
chan = 0
le = 0
temp = 0
while n > 0:
    temp = n % 10
    if temp % 2 == 0:
        chan += 1
    else:
        le += 1
    n //= 10
print(f"chan: {chan}, le: {le}")