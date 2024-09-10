
"""
"""

number = 2
f = 2
e = 2
while e == f:
    print('.', end='')
    a = number * number
    b = str(number)
    d = 0
    for c in b:
        d += int(c)
    e = d - 2
    f = number
    number += 1
print(f)
