def countTwoAndFive(x):
    number2 = number5 = 0
    while x % 2 == 0:
        number2 += 1
        x = x / 2
    while x % 5 == 0:
        number5 += 1
        x = x / 5
    return int(number2), int(number5)
L = [4, 2, 25, 7777777, 100, 3, 77777777, 77777777, 77777777, 77777777]
index = n2 = n5 =0
Number2 = Number5 = [None] * len(L)
while index < len(L):
    Number2[index], Number5[index] = countTwoAndFive(L[index])
    n2 += Number2[index]
    n5 += Number5[index]
    index += 1
print(min(n2,n5))