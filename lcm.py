a = 3
b = 4
c = a
d = b
while d:
    c, d = d, c%d

print(int(a*b/c)) 