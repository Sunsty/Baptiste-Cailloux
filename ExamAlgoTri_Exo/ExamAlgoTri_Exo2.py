# Import

import random

# Variables

myTable = [0]
sizeTab = 0
case1 = 0
case2 = 0
stock = 0

# Code

sizeTab = int(input("Taille tableau ?\n"))
myTable = [0] * sizeTab

for i in range(sizeTab):
    myTable[i] = random.randint(1,50)
print(myTable)

for j in range(sizeTab-1):
    if(myTable[j] > myTable[(j+1)]):
        stock = myTable[j]
        myTable[j] = myTable[(j+1)]
        myTable[(j+1)] = stock

print(myTable)