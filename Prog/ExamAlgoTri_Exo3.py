# Import

import random

# Variables

myTable = [0]
sizeTab = 0
case1 = 0
case2 = 0
stock = 0
isSorted = False
condition = False
l = 0

# Code

sizeTab = int(input("Taille tableau ?\n"))
myTable = [0] * sizeTab

for i in range(sizeTab):
    myTable[i] = random.randint(1,50)
print(myTable)

while(not isSorted):
    for k in range(sizeTab-1):
        if(myTable[k] > myTable[(k+1)]):
            stock = myTable[k]
            myTable[k] = myTable[(k+1)]
            myTable[(k+1)] = stock
    l = 0
    condition = False
    while(not condition and l < (sizeTab-1)):
        if(myTable[l] > myTable[(l+1)]):
            condition = True
            isSorted = False
        else:
            isSorted = True
        l += 1


    print(myTable)

print(f"\nLe tableau à été trié \n{myTable}")