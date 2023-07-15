L = [0, 1, 8, 3, 4]
sortedL = sorted(L)
if len(L) % 2:
    print(sortedL[int((len(L)-1)/2)])
else:
    print((sortedL[int(len(L)/2)]+sortedL[int(len(L)/2-1)])/2)