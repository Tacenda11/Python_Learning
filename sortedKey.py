a = {'b' : 'bb', 'c' : 'cc', 'a' : 'aa'}
listOfA = list(a.keys())
sortedListOfA = sorted(listOfA)
index = 0
while index < len(sortedListOfA)-1:
    print(sortedListOfA[index], end=',')
    index += 1
print(sortedListOfA[index])