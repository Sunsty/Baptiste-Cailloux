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

case1 = int(input("1ere case à échanger ?\n"))
case2 = int(input("2eme case à échanger ?\n"))

stock = myTable[case1]
myTable[case1] = myTable[case2]
myTable[case2] = stock

print(myTable)